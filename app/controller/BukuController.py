from app import db, response, app
from datetime import datetime
from flask import request
# from flask import jsonify, make_response

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


def updateBook(id):
    book = Buku.query.filter_by(nomor_buku=id).first()

    if book == None:
        return response.badRequest('', f'Buku dengan nomor #{id} tidak ada')

    req_data = request.get_json()

    try:
        book.judul = req_data.get('judul')
        book.pengarang = req_data.get('pengarang')
        book.tahun_terbit = req_data.get('tahun_terbit')
        book.penerbit = req_data.get('penerbit')
        book.update_at = datetime.utcnow()

        db.session.commit()
        return response.success(
            '', f'Buku dengan nomor #{id} berhasil di berbaharui !')
    except Exception as e:
        return response.badRequest('', 'Gagal memperbaharui Buku')


def detailBook(id):
    book = Buku.query.filter_by(nomor_buku=id).first()

    if book == None:
        return response.badRequest('', f'Buku dengan nomor #{id} tidak ada')

    data_buku = {
        'nomor_buku': book.nomor_buku,
        'pengarang': book.pengarang,
        'tahun_terbit': book.tahun_terbit,
        'penerbit': book.penerbit,
        'created_at': book.created_at,
        'update_at': book.update_at
    }

    return response.success(data_buku, f'Data Buku')


def createBook():
    req_data = request.get_json()
    nomor_buku = req_data.get('nomor_buku')
    judul = req_data.get('judul')
    pengarang = req_data.get('pengarang')
    tahun_terbit = req_data.get('tahun_terbit')
    penerbit = req_data.get('penerbit')
    create_at = datetime.utcnow()
    update_at = datetime.utcnow()

    buku = Buku.query.filter_by(nomor_buku=nomor_buku).first()

    if buku == None:
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
    else:
        return response.badRequest(
            '', f'Buku dengan nomor #{nomor_buku} sudah ada')


def hapusBook(id):
    book = Buku.query.filter_by(nomor_buku=id).first()

    if book == None:
        return response.badRequest('', f'Buku dengan nomor #{id} tidak ada')
    try:
        db.session.delete(book)
        db.session.commit()
        return response.success('',
                                f'Buku dengan nomor #{id} berhasil di Hapus')
    except Exception as e:
        return response.badRequest('', 'Tidak dapat menghapus')


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
