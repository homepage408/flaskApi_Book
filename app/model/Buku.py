from app import db
from datetime import datetime


class Buku(db.Model):
    nomor_buku = db.Column(db.BigInteger,
                           primary_key=True,
                           autoincrement=False)
    judul = db.Column(db.String(200), nullable=False)
    pengarang = db.Column(db.String(100), nullable=False)
    tahun_terbit = db.Column(db.Integer, nullable=False)
    penerbit = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)