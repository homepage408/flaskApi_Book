from app import db
from app.model.Fakultas import Fakultas


class Prodi(db.Model):
    id_prodi = db.Column(db.Integer, primary_key=True, autoincrement=False)
    nama_prodi = db.Column(db.String(250), nullable=False)
    id_fakultas = db.Column(
        db.Integer, db.ForeignKey(Fakultas.id_fakultas, ondelete='CASCADE'))
