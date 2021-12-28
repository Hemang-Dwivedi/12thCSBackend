from flask import Flask, make_response
from flask_cors import CORS
from pymongo import MongoClient
import datetime

app = Flask(__name__)
DB_URL = 'mongodb+srv://Admin:admin%40123@cluster0.1lkj9.mongodb.net/csproject?retryWrites=true&w=majority'
app = Flask(__name__)
CORS(app)
client = MongoClient(DB_URL)
db = client.csproject


@app.route('/login/<designation>/<userid>/<password>/', methods=['POST'])
def login(designation, userid, password):
    global collec
    if designation == "teacher":
        collec = db.teachers
    elif designation == "student":
        collec = db.students
    user = collec.find_one({'userid': userid})
    if not userid or not password:
        return make_response('Email or password Not Found', 401)
    if not user:
        return make_response('User not found, Please enter a valid user', 402)
    if user['password'] != password:
        return make_response('Incorrect Password', 403)
    var = len(user['present'])
    var2 = 1
    while var2 < var or var2 == var:
        if user['present'][var2 - 1].date() == datetime.datetime.today().date():
            break
        elif var == var2:
            user['present'].append((datetime.datetime.today()))
        var2 = var2 + 1
    collec.replace_one({'userid': userid}, user)
    return make_response('Success', 200)


@app.route('/attend/<designation>/<userid>/', methods=['POST'])
def attendance(designation, userid):
    global collec
    if designation == "teacher":
        collec = db.teachers
    elif designation == "student":
        collec = db.students
    user = collec.find_one({'userid': userid})
    return make_response({'present': user['present']}, 200)
    # return make_response(jsonify({'present': user['present']}), 200)


# if condition to check name is equal to main to generate a script
if __name__ == '__main__':
    # debug=True is used when we didn't saved changes by need output to
    app.run(debug=True)
