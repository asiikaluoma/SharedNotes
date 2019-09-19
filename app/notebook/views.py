from app import app, db
from flask import render_template, request, redirect, url_for
from app.notebook.models import Notebook
from sqlalchemy import desc
from app.notebook.forms import NotebookForm
from flask_login import login_required, current_user

@app.route("/notebook", methods=["GET"])
@login_required
def notebook_index():
    return render_template("notebook/list.html", notebooks = Notebook.query.order_by(desc(Notebook.date_modified)).all())

@app.route("/notebook/new/")
@login_required
def notebook_form():
    return render_template("notebook/new.html", form=NotebookForm())

@app.route("/notebook/", methods=["POST"])
@login_required
def notebook_create():
    form = NotebookForm(request.form)

    if not form.validate():
        return render_template("notebook/new.html", form=form)

    notebook = Notebook(form.title.data)
    notebook.account_id = current_user.id

    db.session().add(notebook)
    db.session().commit()
  
    return redirect(url_for("notebook_index"))