from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class AtoForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    type = db.Column(db.Text(10000))
    os_build = db.Column(db.Text(10000))
    version = db.Column(db.Integer)
    serial_num = db.Column(db.Integer)
    mac_num = db.Column(db.Text(10000))
    creator = db.Column(db.Text(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    date = db.Column(db.DateTime(timezone=True))
    descr = db.Column(db.Text(10000))
    status = db.Column(db.Text(10000))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer)
    role = db.Column(db.Text)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    phone = db.Column(db.Integer)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    ato_forms = db.relationship('AtoForm')

