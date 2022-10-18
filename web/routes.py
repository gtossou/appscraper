from crypt import methods
import os
from .forms import AddProspectAppForm
from flask import(
    Flask,
    url_for,
    render_template,
    redirect,
    request,
    session
)
from dotenv import load_dotenv

from pydantic import ValidationError
from .models import ProspectAppModel

load_dotenv()
DATABASE_URL = os.environ["DATABASE_URL"]

app = Flask(__name__)

app.secret_key = b'\xba\xafg\xd0p|1\x1duh\x7f\x9c\xc65cw\x94\xd0v-\x7f!\xcd\xca\x03\xbdv\xe2\xdc\xf30\xba'

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# TODO : handle  Cross-Site Scripting (XSS) attack


@app.route("/add_prospect_app", methods=["GET", "POST"])
def addapp():
    """Form to add a new app"""
    form = AddProspectAppForm()
    if request.method == "POST":
        for key, val in request.form.items():
            print(f"{key}:{val}")

        try:
            prospect_app_data = ProspectAppModel(
                user_name=request.form['user_name'],
                user_mail=request.form['user_mail'],
                app_name=request.form['app_name'],
                app_url=request.form['app_url']
            )
            session["user_name"] = prospect_app_data.user_name
            session["user_mail"] = prospect_app_data.user_mail
            session["app_name"] = prospect_app_data.app_name
            session["app_url"] = prospect_app_data.app_url
            return redirect(url_for('applist'))
        except ValidationError as e:
            print(e)
    return render_template('add_prospect_app.html', form=form)
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
