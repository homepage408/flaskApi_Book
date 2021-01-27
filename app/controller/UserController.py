from app.model.User import User
from app.model.level_user import Level
from app.model.Mahasiswa import Mahasiswa
from app.model.Prodi import Prodi
from app.model.Fakultas import Fakultas
from app import response, app, db
from flask import request


def CreateUser():
    '''Untuk Membuat User Admin dan Mahasiswa'''
    try:
        # req_data = request.get_json()
        npm = request.form.get('npm')
        nama = request.form.get('nama')
        email = request.form.get('email')
        password = request.form.get('password')
        level = request.form.get('level')

        users = User(npm=npm, nama=nama, email=email, level=level)
        users.setPassword(password)

        db.session.add(users)
        db.session.commit()

        return response.success('', "Berhasil Menambahkan User")

    except Exception as e:
        print(e)


def tampilUser():
    '''Tampil User ini digunakan untuk Menampilkan keseluruhan user yang terdaftar pada table user '''
    try:
        users = User.query.all()
        data = formatArray(users)
        return response.success(data, 'Success')
    except Exception as e:
        # return response.badRequest('', 'Gagal Menampilkan')
        print(e)


def formatArray(datas):
    '''Fungsi ini digunakan untuk melakukan looping terhadap dara user '''
    array = []
    for i in datas:
        array.append(tampilObject(i))
    return array


def tampilObject(data):
    '''Serialize ini digunakan untuk memparsing data dari looping "formatArray" '''
    data = {
        'id_user': data.id_user,
        'npm': data.npm,
        'nama': data.nama,
        'email': data.email,
        'password': data.password,
        'level': data.level
    }
    return data


def tampilDetail():
    '''Fungsi ini digunakan untuk menampilkan data pada table User dengan menggunakan fungsi
    Join untuk mendapatkan nilai yang lebih Detail '''
    users = db.session.query(User.id_user, User.npm, User.nama, User.email,
                             User.password, User.level, Level.id_level,
                             Level.keterangan).join(Level).filter(
                                 User.level == Level.id_level).all()
    # users = db.session.query(
    #     User.id_user, User.npm, User.nama, User.email, User.password,
    #     Level.keterangan, Prodi.nama_prodi, Fakultas.nama_fakultas).join(
    #         Level).join(Mahasiswa).join(Prodi).join(Fakultas).filter(
    #             User.level == Level.id_level and User.npm == Mahasiswa.npm
    #             and Mahasiswa.prodi == Prodi.id_prodi
    #             and Prodi.id_fakultas == Fakultas.id_fakultas).order_by(
    #                 User.id_user).all()

    data = formatArrrayDetail(users)
    return response.success(data, 'Succes')


def formatArrrayDetail(datas):
    '''Ini digunakan untuk melakukan looping terhadap data looping tampil Detail '''
    array = []
    for i in datas:
        array.append(tampilObjectDetail(i))
    return array


def tampilObjectDetail(data):
    '''Digunakan untuk melakukan parsing data dari looping array detail untuk fungsi tampil detail'''
    data = {
        'id_user': data.id_user,
        'npm': data.npm,
        'nama': data.nama,
        'email': data.email,
        'password': data.password,
        'level': data.keterangan,
        # 'prodi': data.nama_prodi,
        # 'fakultas': data.nama_fakultas
    }

    return data