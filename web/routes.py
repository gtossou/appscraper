import os
from ..db.engine import AppInfo
from .forms import AddAppForm
from flask import(
    Flask,
    url_for,
    render_template,
    redirect
)
from dotenv import load_dotenv

DATABASE_URL = os.environ["DATABASE_URL"]

app = Flask(__name__)

load_dotenv()
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@app.route("/AddApp", methods=["GET", "POST"])
def addapp():
    """Form to add a new app"""
    form = AddAppForm()
    return render_template('index.html', form=form)
    # if form.validate_on_submit():
    #     # TODO: extract values from form and make AppInfo object
    #     return redirect(url_for("success"))
    # return render_template(
    #     "contact.jinja2",
    #     form=form,
    #     template="form-template"
    # )
