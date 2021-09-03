from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
import datetime

app = Flask(__name__)
DB_URL = 'mongodb+srv://Admin:admin%40123@cluster0.1lkj9.mongodb.net/csproject?retryWrites=true&w=majority'
CORS(app)
client = MongoClient(DB_URL)
db = client.csproject
col = db.users


def attendance(userid, designation):
    global collec
    if designation == "teacher":
        collec = db.teachers
    elif designation == "student":
        collec = db.students
    user = collec.find_one({'userid': userid})
    for i in user['present']:
        print(i)


attendance('student', 'student')

