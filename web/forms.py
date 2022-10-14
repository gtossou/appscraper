from email import message
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


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
        "Nom de l'App",
        [
            DataRequired()
        ]
    )
    appurl = StringField(
        "Url de l'App (Android Store)",
    )
    # TODO : add recaptcha -> https://john.soban.ski/add-recaptcha-to-your-flask-application.html
    #recaptcha = RecaptchaField()
    submit = SubmitField("Valider")
