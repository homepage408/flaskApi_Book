from app import app
from app.controller import UserController, BukuController
from flask import request


@app.route("/")
def index():
    return "Hello Flask"


@app.route('/createUser', methods=['POST'])
def createUsers():
    return UserController.CreateUser()


@app.route('/tampilUser', methods=['GET'])
def tampilUsers():
    return UserController.tampilUser()


@app.route('/tampilUserDetail', methods=['GET'])
def tampilUsersDetail():
    return UserController.tampilDetail()


@app.route('/books', methods=['GET', 'POST'])
def daftarBuku():
    if request.method == 'GET':
        return BukuController.index()
    else:
        return BukuController.createBook()
