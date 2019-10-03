from app import app, db, login_manager
from flask import render_template, request, redirect, url_for
from app.notes.models import Note
from app.notebook.models import Notebook
from app.auth.models import User
from sqlalchemy import desc
from app.notes.forms import NoteForm
from flask_login import login_required, current_user

def check_user_access(id):
    for obj in current_user.notebooks:
        if str(obj.notebook_id) == str(id):
            return True
    return False

@app.route("/notebook/<notebook_id>/notes", methods=["GET"])
@login_required
def notebook_notes(notebook_id):
    nb = Notebook.query.get(notebook_id)

    if not check_user_access(nb.id):
        return login_manager.unauthorized()

    notes = nb.notes
    for note in notes:
        note.creator = User.query.get(note.creator_id).username
    notes.sort(key=lambda r: r.date_modified, reverse=True)

    is_owner = False
    if current_user.id is nb.owner_id:
        is_owner = True

    return render_template("notes/list.html", notebook=nb, notes=notes, notebook_id=notebook_id, is_owner=is_owner)

@app.route("/notebook/<notebook_id>/notes/<note_id>", methods=["GET"])
@login_required
def notes_view(notebook_id, note_id):

    if not check_user_access(notebook_id):
        return login_manager.unauthorized()

    return render_template("notes/index.html", notebook_id=notebook_id, note=Note.query.get(note_id))

@app.route("/notebook/<notebook_id>/notes/new")
@login_required
def notes_new(notebook_id):

    if not check_user_access(notebook_id):
        return login_manager.unauthorized()

    return render_template("notes/new.html", notebook_id=notebook_id, form=NoteForm())

@app.route("/notebook/<notebook_id>/notes/", methods=["POST"])
@login_required
def notes_create(notebook_id):
    form = NoteForm(request.form)

    if not check_user_access(notebook_id):
        return login_manager.unauthorized()

    if not form.validate():
        return render_template("notes/new.html", form=form)

    note = Note(form.title.data, form.body.data)
    note.notebook_id = notebook_id
    note.creator_id = current_user.id

    db.session().add(note)
    db.session().commit()
  
    return redirect(url_for("notebook_notes", notebook_id=notebook_id))

@app.route("/notebook/<notebook_id>/notes/<note_id>/delete", methods=["POST"])
@login_required
def notes_delete(notebook_id, note_id):

    if not check_user_access(notebook_id):
        return login_manager.unauthorized()

    Note.query.filter_by(id=note_id).delete()
    db.session().commit()
  
    return redirect(url_for("notebook_notes", notebook_id=notebook_id))


@app.route("/notebook/notes/<note_id>/edit")
@login_required
def notes_new_edit(note_id):
    
    if not check_user_access(notebook_id):
        return login_manager.unauthorized()

    n = Note.query.get(note_id)
    form = NoteForm()
    form.title.data = n.title
    form.body.data = n.body
    return render_template("notes/edit.html", note=n, form=form)

@app.route("/notebook/notes/<note_id>/save", methods=["POST"])
@login_required
def notes_edit(note_id):

    if not check_user_access(notebook_id):
        return login_manager.unauthorized()

    form = NoteForm(request.form)

    if not form.validate():
        return render_template("notes/edit.html", form=form)

    note = Note.query.get(note_id)
    note.title = form.title.data
    note.body = form.body.data

    db.session().commit()

    return redirect(url_for('notes_view', notebook_id=note.notebook_id, note_id=note_id))