from app.model.User import User
from app import response, app, db
from flask import request


def CreateUser():
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
