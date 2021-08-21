# import bcrypt
import mongoengine as mongoDB
from flask import Flask, request, make_response
# from flask_bcrypt import Bcrypt
from flask_cors import CORS
from pymongo import MongoClient
# from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
DB_URI = 'mongodb+srv://Admin:admin%40123@cluster0.1lkj9.mongodb.net/csproject?retryWrites=true&w=majority'
mongoDB.connect("csproject", host=DB_URI)
app = Flask(__name__)
CORS(app)
users = MongoClient(DB_URI)


class users(mongoDB.Document):
    userid = mongoDB.StringField(required=True)
    password = mongoDB.StringField(required=True)
    present = mongoDB.DateField(required=False)

    def __init__(self, userid, password, present, *args, **kwargs):
        super(mongoDB.Document, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.password = password
        self.userid = userid
        self.present = present

    def __str__(self):
        return f'userid: {self.userid}, password: {self.password}, present: {self.present} '


@app.route('/login/<userid>/<password>', methods=['GET'])
def login(userid, password):
    user = users.objects(userid=userid).first()
    if not userid or not password:
        return make_response('Email or password Not Found', 401)
    if not user:
        return make_response('User not found, Please enter a valid user', 402)
    if user['password'] != password:
        return make_response('Incorrect Password', 403)
    return make_response('Success', 200)


@app.route('/attendance/<userid>', methods=['POST'])
def attendance(userid):
    user = users.objects(userid=userid).first()
    presentdates = users.objects.present


# if condition to check name is equal to main to generate a script
if __name__ == '__main__':
    # debug=True is used when we didn't saved changes by need output to
    app.run(debug=True)
