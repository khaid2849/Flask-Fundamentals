from flask import Flask, request, render_template, session, redirect, url_for
from flask_migrate import Migrate
from models import db, Accounts
import re

app = Flask(__name__)

app.secret_key = "super secret key"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://khaid:ngoc@localhost:5432/loginandregistration"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    msg = ""
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
    ):
        username = request.form["username"]
        password = request.form["password"]
        account = Accounts.query.filter(
            Accounts.username == username, Accounts.password == password
        ).first()
        if account:
            session["loggedin"] = True
            session["id"] = account.id
            session["username"] = account.username
            msg = "Logged in successfully !"
            return render_template("index.html", msg=msg)
        else:
            msg = "Incorrect username / password !"
    return render_template("login.html", msg=msg)


@app.route("/logout")
def logout():
    session.pop("loggedin", None)
    session.pop("id", None)
    session.pop("username", None)
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    msg = ""
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
        and "email" in request.form
    ):
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        account = Accounts.query.filter(Accounts.username == username).first()
        msg = check_valid_account(account, email, username, password)
    elif request.method == "POST":
        msg = "Please fill out the form !"
    return render_template("register.html", msg=msg)


def check_valid_account(account, email, username, password):
    if account:
        msg = "Account already exists !"
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        msg = "Invalid email address !"
    elif not re.match(r"[A-Za-z0-9]+", username):
        msg = "Username must contain only characters and numbers !"
    elif not username or not password or not email:
        msg = "Please fill out the form !"
    else:
        account = Accounts(username=username, password=password, email=email)
        db.session.add(account)
        db.session.commit()
        msg = "You have successfully registered !"
    return msg
