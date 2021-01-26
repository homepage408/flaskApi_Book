from app import db
from app.model.Prodi import Prodi
from app.model.Fakultas import Fakultas


class Mahasiswa(db.Model):
    npm = db.Column(db.BigInteger, primary_key=True, autoincrement=False)
    nama = db.Column(db.String(200), nullable=False)
    no_hp = db.Column(db.BigInteger, nullable=False)
    angkatan = db.Column(db.Integer, nullable=False)
    alamat = db.Column(db.String(200), nullable=False)
    prodi = db.Column(db.Integer,
                      db.ForeignKey(Prodi.id_prodi, ondelete='CASCADE'))
