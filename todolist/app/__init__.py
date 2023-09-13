from flask import Flask
from flask_migrate import Migrate
from .models import db
from .routes import todo_bp


def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object("config.Config")

    # Initialize the database extension
    db.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprints
    app.register_blueprint(todo_bp)

    return app
