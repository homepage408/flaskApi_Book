from app import db
from datetime import datetime
from app.model.Mahasiswa import Mahasiswa
from app.model.level_user import Level
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    npm = db.Column(db.BigInteger,
                    db.ForeignKey(Mahasiswa.npm, ondelete='CASCADE'))
    nama = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    level = db.Column(db.Integer,
                      db.ForeignKey(Level.id_level, ondelete='CASCADE'))

    def __repr__(self):
        return '<User {}>'.format(self.nama)

    def setPassword(self, password):
        self.password = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)
