from app import app, db
from flask import render_template, request, redirect, url_for
from app.notes.models import Note
from sqlalchemy import desc

@app.route("/notebook/<notebook_id>/notes", methods=["GET"])
def notebook_notes(notebook_id):
    return render_template("notes/list.html", notes=Note.query.order_by(desc(Note.date_modified)).all(), notebook_id=notebook_id)

@app.route("/notebook/<notebook_id>/notes/<note_id>", methods=["GET"])
def notes(notebook_id, note_id):
    return render_template("notes/index.html", note=Note.query.get(note_id))

@app.route("/notebook/<notebook_id>/notes/new")
def notes_new(notebook_id):
    return render_template("notes/new.html", notebook_id=notebook_id)

@app.route("/notebook/<notebook_id>/notes/", methods=["POST"])
def notes_create(notebook_id):
    t = Note(request.form.get("title"), request.form.get("body"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("notebook_notes", notebook_id=notebook_id))