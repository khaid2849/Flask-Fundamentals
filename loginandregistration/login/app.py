from flask import Flask, request, render_template, session
from flask_sqlalchemy import SQLAlchemy
from models import Accounts

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://khaid:ngoc@localhost:5432/loginandregistration"
db = SQLAlchemy(app)
db.init_app(app)


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
            session["id"] = account["id"]
            session["username"] = account["username"]
            msg = "Logged in successfully !"
            return render_template("index.html", msg=msg)
        else:
            msg = "Incorrect username / password !"
    return render_template("login.html", msg=msg)
