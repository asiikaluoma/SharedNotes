from flask import render_template, redirect, url_for
from app import app
from app.notebook import views

@app.route("/")
def index():
    return redirect(url_for('notebook_index'))