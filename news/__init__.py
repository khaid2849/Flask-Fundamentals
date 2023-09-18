from flask import Flask
from news.main.controller.routes import news_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(news_bp)

    return app
