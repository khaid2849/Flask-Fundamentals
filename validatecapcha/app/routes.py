from flask import render_template, request
from flask_session_captcha import FlaskSessionCaptcha

from validatecapcha.app import create_app, validate_bp


captcha = FlaskSessionCaptcha(create_app())


@validate_bp.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if captcha.validate():
            return "success"
        else:
            return "fail"
    return render_template("form.html")
