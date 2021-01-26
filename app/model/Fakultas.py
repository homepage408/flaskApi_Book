from app import db


class Fakultas(db.Model):
    id_fakultas = db.Column(db.Integer, primary_key=True, autoincrement=False)
    nama_fakultas = db.Column(db.String(250), nullable=False)