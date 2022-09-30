from flask import(
    Flask,
    url_for,
    render_template,
    redirect
)
from .forms import AddAppForm
from ..db.engine import AppInfo

app = Flask(__name__)


@app.route("/AddApp", methods=["GET", "POST"])
def addapp():
    """Form to add a new app"""
    form = AddAppForm()
    if form.validate_on_submit():
        # TODO: extract values from form and make AppInfo object
        return redirect(url_for("success"))
    return render_template(
        "contact.jinja2",
        form=form,
        template="form-template"
    )
