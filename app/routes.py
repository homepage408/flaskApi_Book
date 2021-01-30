from app import app
from app.controller import UserController, BukuController, MahasiswaController
from flask import request


# Error Handler
@app.errorhandler(404)
def page_not_found(e):
    return {'Error': 'Page is not found'}


@app.route("/")
def index():
    return "Hello Flask"


# User
@app.route('/user', methods=['GET', 'POST'])
def createUsers():
    if request.method == 'GET':
        return UserController.CreateUser()
    else:
        return UserController.tampilUser()


@app.route('/tampilUserDetail', methods=['GET'])
def tampilUsersDetail():
    return UserController.tampilDetail()


# Buku
@app.route('/books', methods=['GET', 'POST'])
def daftarBuku():
    if request.method == 'GET':
        return BukuController.index()
    else:
        return BukuController.createBook()


@app.route('/book/<id>', methods=['GET', 'PUT', 'DELETE'])
def update_Book(id):
    if request.method == 'PUT':
        return BukuController.updateBook(id)
    elif request.method == 'GET':
        return BukuController.detailBook(id)
    else:
        return BukuController.hapusBook(id)


@app.route('/mahasiswa', methods=['GET', 'POST'])
def detailMahasiswa():
    if request.method == 'GET':
        return MahasiswaController.detailMahasiwa()
    else:
        return MahasiswaController.saveMahasiswa()


@app.route('/mahasiswa/<npm>', methods=['GET', 'PUT', 'DELETE'])
def detailMahasiswabynpm(npm):
    if request.method == 'GET':
        return MahasiswaController.detailMahasiswabynpm(npm)
    elif request.method == 'PUT':
        return MahasiswaController.editMahasiswa(npm)
    else:
        return MahasiswaController.deleteMahasiswa(npm)
