from app import db
from flask_login import UserMixin
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    last_name = db.Column(db.String(1000))
    def __repr__(self):
        return '<User %r>' % self.username

