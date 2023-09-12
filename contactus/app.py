from flask import Flask, render_template
from form import ContactForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "secret key"

Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def home():
    cform = ContactForm()
    if cform.validate_on_submit():
        print(
            f"Name:{cform.name.data}, E-mail:{cform.email.data},message:{cform.message.data}"
        )
    return render_template("contact.html", form=cform)
