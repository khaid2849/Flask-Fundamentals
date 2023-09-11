from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_restx import Api, Resource
from datetime import timedelta
from models import User
from database import db_session, init_db

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
# app.config["SQLACHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)
init_db()
# db = SQLAlchemy(app)


# class users(db.Model):
#     _id = db.Column("id", db.Integer, primary_key=True)
#     name = db.Column("name", db.String(100))
#     email = db.Column("email", db.String(100))

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# api = Api(
#     app=app,
#     doc="/docs",
#     version="1.0",
#     title="Khaid API",
#     description="Khaid - Flask - API",
#     default="Flask",
#     default_label="Flask-Fundamentals",
# )


# @api.route("/hello")
# class HelloWorld(Resource):
#     def get(self):
#         return {"hello": "world"}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]

        found_user = User.query.filter(User.name == user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = User(user, "")
            db_session.add(usr)
            db_session.commit()

        session["user"] = user
        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return render_template(url_for("user"))
        return render_template("login.html")


@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email

            found_user = User.query.filter(User.name == user).first()
            found_user.email = email
            db_session.commit()
            flash("Email was saved")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email=email)
    else:
        flash("You are not Logged In!")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


@app.route("/view")
def view():
    return render_template("view.html", values=User.query.all())
