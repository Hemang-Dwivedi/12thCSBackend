# import bcrypt
# import mongoengine as mongoDB
from flask import Flask, make_response
# from flask_bcrypt import Bcrypt
from flask_cors import CORS
from pymongo import MongoClient
from bson import json_util
import json

app = Flask(__name__)
DB_URL = 'mongodb+srv://Admin:admin%40123@cluster0.1lkj9.mongodb.net/csproject?retryWrites=true&w=majority'
app = Flask(__name__)
CORS(app)
client = MongoClient(DB_URL)
db = client.csproject
col = db.users


@app.route('/login/<userid>/<password>', methods=['GET'])
def login(userid, password):
    user = col.find_one({'userid': userid})
    if not userid or not password:
        return make_response('Email or password Not Found', 401)
    if not user:
        return make_response('User not found, Please enter a valid user', 402)
    if user['password'] != password:
        return make_response('Incorrect Password', 403)
    return make_response('Success', 200)


@app.route('/attendance/<userid>', methods=['POST'])
def attendance(userid):
    user = col.find_one({'userid': userid})
    user = json.dumps(json_util.dumps(user))
    # present = col.find_one()
    return make_response(user, 200)


# if condition to check name is equal to main to generate a script
if __name__ == '__main__':
    # debug=True is used when we didn't saved changes by need output to
    app.run(debug=True)
