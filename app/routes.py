from app import app
# from app.controller import UserControll
from app.controller import UserControll
from flask import request


@app.route("/")
def index():
    return "Hello Flask"


@app.route('/createUser', methods=['POST'])
def createUsers():
    return UserControll.CreateUser()
