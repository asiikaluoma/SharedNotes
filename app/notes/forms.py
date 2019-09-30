from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField

class NoteForm(FlaskForm):
    title = StringField("Note title", [validators.Length(min=1, max=100)])
    body = TextAreaField("Body", [validators.Length(min=1, max=10000)])
 
    class Meta:
        csrf = False