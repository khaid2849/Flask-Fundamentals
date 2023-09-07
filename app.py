from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(
    app=app,
    doc="/docs",
    version="1.0",
    title="Khaid API",
    description="Khaid - Flask - API",
    default="Flask",
    default_label="Flask-Fundamentals",
)


@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}
