from crypt import methods
import os
from .forms import AddAppForm
from flask import(
    Flask,
    url_for,
    render_template,
    redirect,
    request,
    session
)
from dotenv import load_dotenv

from pydantic import BaseModel, validator, EmailStr, ValidationError


class AddAppModel(BaseModel):
    """Class for parsing new stock data from a form."""
    user_name: str
    user_mail: EmailStr
    app_name: str
    app_url: str

    # @validator('stock_symbol')
    # def stock_symbol_check(cls, value):
    #     if not value.isalpha() or len(value) > 5:
    #         raise ValueError('Stock symbol must be 1-5 characters')
    #     return value.upper()


DATABASE_URL = os.environ["DATABASE_URL"]

app = Flask(__name__)

app.secret_key = b'\xba\xafg\xd0p|1\x1duh\x7f\x9c\xc65cw\x94\xd0v-\x7f!\xcd\xca\x03\xbdv\xe2\xdc\xf30\xba'

load_dotenv()
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# TODO : handle  Cross-Site Scripting (XSS) attack


@app.route("/add_app", methods=["GET", "POST"])
def addapp():
    """Form to add a new app"""
    form = AddAppForm()
    if request.method == "POST":
        for key, val in request.form.items():
            print(f"{key}:{val}")

        try:
            new_app_data = AddAppModel(
                user_name=request.form['user_name'],
                user_mail=request.form['user_mail'],
                app_name=request.form['app_name'],
                app_url=request.form['app_url']
            )
            session["user_name"] = new_app_data.user_name
            session["user_mail"] = new_app_data.user_mail
            session["app_name"] = new_app_data.app_name
            session["app_url"] = new_app_data.app_url
            return redirect(url_for('applist'))
        except ValidationError as e:
            print(e)
    return render_template('add_app.html', form=form)
    # if form.validate_on_submit():
    #     # TODO: extract values from form and make AppInfo object
    #     return redirect(url_for("success"))
    # return render_template(
    #     "contact.jinja2",
    #     form=form,
    #     template="form-template"
    # )


@app.route("/app_list", methods=["GET", "POST"])
def applist():
    """Form to list new apps"""
    # form = AppListForm()
    # if request.method == "POST":
    #     pass
    return render_template('app_list.html')
