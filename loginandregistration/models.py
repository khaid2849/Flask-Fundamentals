from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


db = SQLAlchemy()


class Accounts(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(255))
    email = db.Column(db.String(100))

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f"<Account {self.username}>"
