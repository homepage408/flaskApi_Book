from app.model.Mahasiswa import Mahasiswa
from app.model.Prodi import Prodi
from app.model.Fakultas import Fakultas
from app import app, db, response
from flask import request


def tampilMahasiswa():
    try:
        mhs = Mahasiswa.query.all()
        if data is None:
            return response.badRequest("", "Tidak ada data mahasiswa")

        data = [serializeMahasiswa(data) for data in mhs]
        return response.success(data, "Success")
    except Exception as e:
        return response.badRequest("", "Tidak dapat menampilkan")


def detailMahasiwa():
    try:
        dataMhs = db.session.query(Mahasiswa.npm, Mahasiswa.nama, Mahasiswa.no_hp, Mahasiswa.angkatan, Mahasiswa.alamat, Prodi.nama_prodi, Fakultas.nama_fakultas).select_from(Mahasiswa).join(
            Prodi).join(Fakultas).filter(Mahasiswa.prodi == Prodi.id_prodi and Prodi.id_fakultas == Fakultas.id_fakultas).all()

        if dataMhs is None:
            return response.badRequest('', 'Data tidak ada')

        # data = [serializeDetailMahasiswa(data) for data in dataMhs]
        data = formatarray(dataMhs)
        return response.success(data, 'Success')
    except Exception as e:
        print(e)


def serializeMahasiswa(data):
    data = {
        "npm": data.npm,
        "nama": data.nama,
        "no_hp": data.no_hp,
        "angkatan": data.angkatan,
        "alamat": data.alamat,
        "prodi": data.prodi,
    }
    return data


def formatarray(datas):
    array = []
    for i in datas:
        array.append(serializeDetailMahasiswa(i))
    print(array)
    return array


def serializeDetailMahasiswa(data):
    data = {
        "npm": data.npm,
        "nama": data.nama,
        "no_hp": data.no_hp,
        "angkatan": data.angkatan,
        "alamat": data.alamat,
        "nama_prodi": data.nama_prodi,
        "nama_fakultas": data.nama_fakultas,
    }
    return data
