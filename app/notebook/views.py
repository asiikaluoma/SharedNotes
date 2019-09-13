from app import app, db
from flask import render_template, request, redirect, url_for
from app.notebook.models import Notebook
from sqlalchemy import desc

@app.route("/notebook", methods=["GET"])
def notebook_index():
    return render_template("notebook/list.html", notebooks = Notebook.query.order_by(desc(Notebook.date_modified)).all())

@app.route("/notebook/new/")
def notebook_form():
    return render_template("notebook/new.html")

@app.route("/notebook/", methods=["POST"])
def notebook_create():
    t = Notebook(request.form.get("title"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("notebook_index"))