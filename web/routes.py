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
# from .models import ProspectAppModel
from ..db.db_models import AppProspect
from ..db.engine import create_sql_engine
from sqlmodel import Session, SQLModel, select
import logging


logging.getLogger().setLevel(logging.INFO)
load_dotenv()
DATABASE_URL = os.environ["DATABASE_URL"]

app = Flask(__name__)

app.secret_key = b'\xba\xafg\xd0p|1\x1duh\x7f\x9c\xc65cw\x94\xd0v-\x7f!\xcd\xca\x03\xbdv\xe2\xdc\xf30\xba'

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# TODO : handle  Cross-Site Scripting (XSS) attack


def insert_app_prospect(db_session, prospect_app_data):
    '''
    Insert into db model AppProspect

            Parameters:

                session (str): database session
                prospect_app_data ?

            Returns:
                Inserted data
    '''
    # Check if appurl already exists
    app_exists_query = select(AppProspect).where(
        AppProspect.appurl == prospect_app_data.appurl)
    app_ = db_session.exec(statement=app_exists_query).one_or_none()
    if app_ is not None:
        logging.warning("Prospect app already exists")
    # TODO show warning in the dom ?
    else:
        logging.info("Inserting new app prospect into db")
        db_session.add(prospect_app_data)
        db_session.commit()


@app.route("/add_prospect_app", methods=["GET", "POST"])
def add_app_prospect():
    """Form to add a new app"""
    form = AddProspectAppForm()
    if request.method == "POST":
        for key, val in request.form.items():
            print(f"{key}:{val}")

        try:
            prospect_app_data = AppProspect(
                username=request.form['user_name'],
                email=request.form['user_mail'],
                appname=request.form['app_name'],
                appurl=request.form['app_url']
            )
            # session["user_name"] = prospect_app_data.username
            # session["user_mail"] = prospect_app_data.email
            # session["app_name"] = prospect_app_data.appname
            # session["app_url"] = prospect_app_data.appurl

            engine_ = create_sql_engine()
            if engine_ is not None:
                SQLModel.metadata.create_all(engine_)

            with Session(engine_) as db_session:
                insert_app_prospect(db_session, prospect_app_data)
            return redirect(url_for('show_app_list'))
        except ValidationError as e:
            print(e)
    return render_template('add_prospect_app.html', form=form)


@app.route("/app_list", methods=["GET", "POST"])
def show_app_list():
    """Form to list new apps"""

    return render_template('app_list.html')
