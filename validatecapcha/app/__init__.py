from flask import Flask, Blueprint
from flask_sessionstore import Session

validate_bp = Blueprint(
    "validate_bp", __name__, template_folder="templates", url_prefix="/validate"
)


def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object("config.Config")

    # # Initialize the database extension
    Session(app)

    # Register blueprints
    app.register_blueprint(validate_bp)

    return app
