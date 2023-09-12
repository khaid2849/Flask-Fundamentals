from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
import email_validator


class ContactForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    email = StringField(
        label="Email", validators=[DataRequired(), Email(granular_message=True)]
    )
    message = StringField(label="Message", validators=[DataRequired()])
    submit = SubmitField(label="Send")
