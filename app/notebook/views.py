from app import app, db
from flask import render_template, request, redirect, url_for
from app.notebook.models import Notebook
from sqlalchemy import desc
from app.notebook.forms import NotebookForm
from flask_login import login_required, current_user
from app.auth.models import UserNotebook, User

@app.route("/notebook", methods=["GET"])
@login_required
def notebook_index():
    notebooks = list(map(lambda x: x.child, current_user.notebooks))
    return render_template("notebook/list.html", notebooks=notebooks)

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

    notebook = Notebook(form.title.data, form.description.data)
    notebook.owner_id = current_user.id

    db.session().add(notebook)
    db.session().flush()

    user = User.query.get(current_user.id)
    a = UserNotebook()
    a.account_id = notebook.owner_id
    a.child = Notebook.query.get(notebook.id)
    user.notebooks.append(a)

    db.session().commit()
  
    return redirect(url_for("notebook_index"))


@app.route("/notebook/<notebook_id>/edit")
def notebook_new_edit(notebook_id):
    n = Notebook.query.get(notebook_id)

    is_owner = False
    if current_user.id == n.owner_id:
        is_owner = True
    
    error_param = request.args.get("error")

    form = NotebookForm()
    form.title.data = n.title
    form.description.data = n.description
    return render_template("notebook/edit.html", notebook=n, form=form, is_owner=is_owner, error=error_param)


@app.route("/notebook/<notebook_id>/user", methods=["POST"])
def notebook_add_user(notebook_id):
    notebook = Notebook.query.get(notebook_id)
    if current_user.id != notebook.owner_id:
        return redirect(url_for('notebook_new_edit', notebook_id=notebook_id))

    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()

    if user is None:
        return redirect(url_for('notebook_new_edit', notebook_id=notebook_id, error="User not found."))
    
    if any(x.notebook_id == notebook_id for x in user.notebooks):
        return redirect(url_for('notebook_new_edit', notebook_id=notebook_id, error="User already added."))

    a = UserNotebook()
    a.account_id = user.id
    a.child = notebook
    user.notebooks.append(a)

    db.session().commit()
  

    return redirect(url_for('notebook_new_edit', notebook_id=notebook_id))

@app.route("/notebook/<notebook_id>/save", methods=["POST"])
def notebook_edit(notebook_id):
    form = NotebookForm(request.form)

    if not form.validate():
        return render_template("notebook/edit.html", form=form)

    n = Notebook.query.get(note_id)
    n.title = form.title.data
    n.description = form.description.data

    db.session().commit()

    return redirect(url_for('notebook_index'))