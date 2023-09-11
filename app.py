from flask import Flask, redirect, url_for, render_template, request, session
from flask_restx import Api, Resource
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

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
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return render_template(url_for("user"))
        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
