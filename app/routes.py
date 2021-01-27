from app import app
from app.controller import UserController, BukuController
from flask import request


@app.route("/")
def index():
    return "Hello Flask"


@app.route('/user', methods=['GET', 'POST'])
def createUsers():
    if request.method == 'GET':
        return UserController.CreateUser()
    else:
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
