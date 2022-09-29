from email import message
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length


class AddAppForm(FlaskForm):
    """New app form"""
    username = StringField(
        "Votre nom",
        [DataRequired()]
    )
    mail = StringField(
        "Email",
        [
            Email(message=('Not a valid email address.')),
            DataRequired()
        ]
    )
    appname = StringField(
        "Nom de l'application mobile",
        [
            DataRequired()
        ]
    )
    appurl = StringField(
        "Url de l'application mobile",
    )

    recaptcha = RecaptchaField()
    submit = SubmitField("Valider")
