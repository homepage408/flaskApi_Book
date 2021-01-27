from app import db, response, app
from datetime import datetime
from flask import request

from app.model.Buku import Buku


def index():
    '''Menampilkan daftar buku yang terdapar pada table buku '''
    try:
        books = Buku.query.all()
        data_buku = fromatArrayBooks(books)
        return response.success(data_buku, 'Success')
    except Exception as e:
        return response.badRequest('', 'Gagal Menampilkan')
        # print(e)


def fromatArrayBooks(datas):
    array = []
    for i in datas:
        array.append(singleObjectBooks(i))
    return array


def singleObjectBooks(data):
    '''Parsing data looping Books '''
    data = {
        'nomor_buku': data.nomor_buku,
        'judul': data.judul,
        'pengarang': data.pengarang,
        'tahun_terbit': data.tahun_terbit,
        'penerbit': data.penerbit,
        'creat_at': data.created_at,
        'update_at': data.update_at
    }
    return data


def createBook():
    req_data = request.get_json()
    nomor_buku = req_data.get('nomor_buku')
    judul = req_data.get('judul')
    pengarang = req_data.get('pengarang')
    tahun_terbit = req_data.get('tahun_terbit')
    penerbit = req_data.get('penerbit')
    create_at = datetime.utcnow()
    update_at = datetime.utcnow()

    book = Buku(nomor_buku=nomor_buku,
                judul=judul,
                pengarang=pengarang,
                tahun_terbit=tahun_terbit,
                penerbit=penerbit,
                created_at=create_at,
                update_at=update_at)

    try:
        db.session.add(book)
        db.session.commit()
        return response.success('', 'Berhasil Mebambahkan Buku')
    except Exception as e:
        return response.badRequest('', 'Gagal menambahkan Buku !!!')
