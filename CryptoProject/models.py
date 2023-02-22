from CryptoProject import db, login_manager
from flask_login import UserMixin
from enum import Enum


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(25), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(60), nullable=False)
    city = db.Column(db.String(25), nullable=False)
    state = db.Column(db.String(25), nullable=False)
    cellphone = db.Column(db.Integer, unique=True, nullable=False)
    validated = db.Column(db.Boolean, nullable=False, default=False)
    transactions = db.relationship('Transaction', backref='creator', lazy=True)
    money = db.Column(db.Float, nullable=False, default=0.0)
    bitcoin = db.Column(db.Float, nullable=False, default=0.0)
    dogecoin = db.Column(db.Float, nullable=False, default=0.0)
    litecoin = db.Column(db.Float, nullable=False, default=0.0)
    ripple = db.Column(db.Float, nullable=False, default=0.0)
    ethereum = db.Column(db.Float, nullable=False, default=0.0)


class Transaction(db.Model):
    id = db.Column(db.String(120), primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String, nullable=False)
    status = db.Column(db.String(20), nullable=False)


class Status(Enum):
    IN_PROGRESS = 1
    COMPLETED = 2
    DENIED = 3
