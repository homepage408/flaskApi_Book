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

        data = [serializeDetailMahasiswa(data) for data in dataMhs]
        # data = formatarray(dataMhs)
        # data = serializeDetailMahasiswa(dataMhs)
        return response.success(data, 'Success')
    except Exception as e:
        print(e)


def saveMahasiswa():
    try:
        data_req = request.get_json()
        npm = data_req.get('npm')
        nama = data_req.get('nama')
        no_hp = data_req.get('no_hp')
        angkatan = data_req.get('angkatan')
        alamat = data_req.get('alamat')
        prodi = data_req.get('prodi')

        mahasiswa = Mahasiswa.query.filter_by(npm=npm).first()

        if mahasiswa is None:
            data = Mahasiswa(npm=npm, nama=nama, no_hp=no_hp,
                             angkatan=angkatan, alamat=alamat, prodi=prodi)

            try:
                db.session.add(data)
                db.session.commit()

                return response.success('', 'Data Berhasil di tambahkan')
            except Exception as e:
                return response.badRequest('', 'Data Gagal di tambahkan')
        else:
            return response.badRequest('', f'Mahasiswa dengan npm #{npm} sudah ada')
    except Exception as e:
        print(e)


def detailMahasiswabynpm(npm):
    try:
        dataMhs = db.session.query(Mahasiswa.npm, Mahasiswa.nama, Mahasiswa.no_hp, Mahasiswa.angkatan, Mahasiswa.alamat, Prodi.nama_prodi, Fakultas.nama_fakultas).select_from(Mahasiswa).join(
            Prodi).join(Fakultas).filter(Mahasiswa.npm == npm and Mahasiswa.prodi == Prodi.id_prodi and Prodi.id_fakultas == Fakultas.id_fakultas).first()

        if dataMhs is None:
            return response.badRequest('', 'Data tidak ditemukan')

        data = serializeDetailMahasiswa(dataMhs)
        return response.success(data, 'Success')
    except Exception as e:
        return response.badRequest('', 'Gagal menampilkan')


def editMahasiswa(npm):
    mhs = Mahasiswa.query.filter_by(npm=npm).first()

    if mhs is None:
        return response.badRequest('', f'Mahasiswa dengan NPM #{npm} tidak ada')

    req_data = request.get_json()

    mhs.npm = req_data.get('npm')
    mhs.nama = req_data.get('nama')
    mhs.no_hp = req_data.get('no_hp')
    mhs.angakatan = req_data.get('angkatan')
    mhs.alamat = req_data.get('alamat')
    mhs.prodi = req_data.get('prodi')

    try:
        db.session.commit()
        return response.success('', 'Success')
    except Exception as e:
        return response.badRequest('', 'Gagal Update Mahasiswa')


def deleteMahasiswa(npm):
    mhs = Mahasiswa.query(npm=npm).first()

    if mhs is None:
        return response.badRequest('', f'Mahasiswa dengan NPM #{npm} tidak ada')

    try:
        db.session.delete(mhs)
        db.session.commit()
        return response.success('', 'Success')
    except Exception as e:
        return response.badRequest('', 'Gagal Menambahkan')


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
