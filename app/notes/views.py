from app import app, db
from flask import render_template, request, redirect, url_for
from app.notes.models import Note
from sqlalchemy import desc

@app.route("/notebook/<notebook_id>/notes", methods=["GET"])
def notebook_notes(notebook_id):
    return render_template("notes/list.html", notes=Note.query.order_by(desc(Note.date_modified)).all(), notebook_id=notebook_id)

@app.route("/notebook/<notebook_id>/notes/<note_id>", methods=["GET"])
def notes_view(notebook_id, note_id):
    return render_template("notes/index.html", notebook_id=notebook_id, note=Note.query.get(note_id))

@app.route("/notebook/<notebook_id>/notes/new")
def notes_new(notebook_id):
    return render_template("notes/new.html", notebook_id=notebook_id)

@app.route("/notebook/<notebook_id>/notes/", methods=["POST"])
def notes_create(notebook_id):
    t = Note(request.form.get("title"), request.form.get("body"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("notebook_notes", notebook_id=notebook_id))

@app.route("/notebook/<notebook_id>/notes/<note_id>/delete", methods=["POST"])
def notes_delete(notebook_id, note_id):
    Note.query.filter_by(id=note_id).delete()
    db.session().commit()
  
    return redirect(url_for("notebook_notes", notebook_id=notebook_id))


@app.route("/notebook/notes/<note_id>/edit")
def notes_new_edit(note_id):
    return render_template("notes/edit.html", note=Note.query.get(note_id))

@app.route("/notebook/notes/<note_id>/save", methods=["POST"])
def notes_edit(note_id):
    note = Note.query.get(note_id)
    note.title = request.form.get("title")
    note.body = request.form.get("body")
    db.session().commit()

    return redirect(url_for('notes_view', notebook_id=1, note_id=note_id))