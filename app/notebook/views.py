from app import app, db, login_manager
from flask import render_template, request, redirect, url_for
from app.notebook.models import Notebook
from sqlalchemy import desc
from app.notebook.forms import NotebookForm
from flask_login import login_required, current_user
from app.auth.models import UserNotebook, User
from app.notes.models import Note

@app.route("/notebook", methods=["GET"])
@login_required
def notebook_index():
    notebooks = list(map(lambda x: x.child, current_user.notebooks))
    print(notebooks)
    return render_template("notebook/list.html", notebooks=notebooks, stats=User.user_notebook_note_counts(current_user.id))

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
@login_required
def notebook_new_edit(notebook_id):
    n = Notebook.query.get(notebook_id)

    if current_user.id is not n.owner_id:
        return login_manager.unauthorized()

    is_owner = False
    if current_user.id == n.owner_id:
        is_owner = True
    
    error_param = request.args.get("error")

    form = NotebookForm()
    form.title.data = n.title
    form.description.data = n.description
    return render_template("notebook/edit.html", notebook=n, form=form, is_owner=is_owner, error=error_param)


@app.route("/notebook/<notebook_id>/user", methods=["POST"])
@login_required
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

@app.route("/notebook/<notebook_id>/user/<user_id>", methods=["POST"])
@login_required
def notebook_delete_user(notebook_id,user_id):
    notebook = Notebook.query.get(notebook_id)
    if current_user.id != notebook.owner_id:
        return redirect(url_for('notebook_new_edit', notebook_id=notebook_id))
    user = User.query.filter_by(id=user_id).first()

    if user is None:
        return redirect(url_for('notebook_new_edit', notebook_id=notebook_id, error="User not found."))

    if user_id == notebook.owner_id:
        return redirect(url_for('notebook_new_edit', notebook_id=notebook_id, error="Cannot delete user right from owner."))

    if any(x.notebook_id == notebook_id for x in user.notebooks):
        return redirect(url_for('notebook_new_edit', notebook_id=notebook_id, error="User already added."))
    
    db.session().query(UserNotebook).filter(UserNotebook.account_id==user_id, UserNotebook.notebook_id==notebook_id).delete()
    db.session().commit()
  
    return redirect(url_for('notebook_new_edit', notebook_id=notebook_id))

@app.route("/notebook/<notebook_id>/save", methods=["POST"])
@login_required
def notebook_edit(notebook_id):

    n = Notebook.query.get(notebook_id)

    if current_user.id is not n.owner_id:
        return login_manager.unauthorized()

    form = NotebookForm(request.form)

    if not form.validate():
        return render_template("notebook/edit.html", form=form)

    n.title = form.title.data
    n.description = form.description.data

    db.session().commit()

    return redirect(url_for('notebook_index'))

@app.route("/notebook/<notebook_id>/delete", methods=["POST"])
@login_required
def notebook_delete(notebook_id):

    n = Notebook.query.get(notebook_id)

    if current_user.id is not n.owner_id:
        return login_manager.unauthorized()
    
    n_id = n.id
    db.session().query(UserNotebook).filter(UserNotebook.notebook_id==n_id).delete()
    db.session().query(Note).filter(Note.notebook_id==n_id).delete()
    Notebook.query.filter_by(id=n_id).delete()

    db.session().commit()
  
    return redirect(url_for("notebook_index"))
