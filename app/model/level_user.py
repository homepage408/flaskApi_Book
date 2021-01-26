from app import db


class Level(db.Model):
    id_level = db.Column(db.Integer, primary_key=True, autoincrement=False)
    keterangan = db.Column(db.String(200), nullable=False)
