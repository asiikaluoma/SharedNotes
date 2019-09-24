from app import app, db
from flask import render_template, request, redirect, url_for
from app.notes.models import Note
from app.notebook.models import Notebook
from app.auth.models import User
from sqlalchemy import desc
from app.notes.forms import NoteForm
from flask_login import login_required, current_user

@app.route("/notebook/<notebook_id>/notes", methods=["GET"])
def notebook_notes(notebook_id):
    notes = Notebook.query.get(notebook_id).notes
    for note in notes:
        note.creator = User.query.get(note.id).username
    return render_template("notes/list.html", notes=Notebook.query.get(notebook_id).notes, notebook_id=notebook_id)

@app.route("/notebook/<notebook_id>/notes/<note_id>", methods=["GET"])
def notes_view(notebook_id, note_id):
    return render_template("notes/index.html", notebook_id=notebook_id, note=Note.query.get(note_id))

@app.route("/notebook/<notebook_id>/notes/new")
def notes_new(notebook_id):
    return render_template("notes/new.html", notebook_id=notebook_id, form=NoteForm())

@app.route("/notebook/<notebook_id>/notes/", methods=["POST"])
def notes_create(notebook_id):
    form = NoteForm(request.form)

    if not form.validate():
        return render_template("notes/new.html", form=form)

    note = Note(form.title.data, form.body.data)
    note.notebook_id = notebook_id
    note.creator_id = current_user.id

    db.session().add(note)
    db.session().commit()
  
    return redirect(url_for("notebook_notes", notebook_id=notebook_id))

@app.route("/notebook/<notebook_id>/notes/<note_id>/delete", methods=["POST"])
def notes_delete(notebook_id, note_id):
    Note.query.filter_by(id=note_id).delete()
    db.session().commit()
  
    return redirect(url_for("notebook_notes", notebook_id=notebook_id))


@app.route("/notebook/notes/<note_id>/edit")
def notes_new_edit(note_id):
    n = Note.query.get(note_id)
    form = NoteForm()
    form.title.data = n.title
    form.body.data = n.body
    return render_template("notes/edit.html", note=n, form=form)

@app.route("/notebook/notes/<note_id>/save", methods=["POST"])
def notes_edit(note_id):
    form = NoteForm(request.form)

    if not form.validate():
        return render_template("notes/edit.html", form=form)

    note = Note.query.get(note_id)
    note.title = form.title.data
    note.body = form.body.data

    db.session().commit()

    return redirect(url_for('notes_view', notebook_id=1, note_id=note_id))