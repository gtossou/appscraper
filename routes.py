from flask import(
    Flask,
    url_for,
    render_template,
    redirect
)
from .forms import AddAppForm

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')


@app.route("/AddApp", methods=["GET", "POST"])
def addapp():
    """Form to add a new app"""
    form = AddAppForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "contact.jinja2",
        form=form,
        template="form-template"
    )
