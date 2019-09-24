from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField

class NoteForm(FlaskForm):
    title = StringField("Note title", [validators.Length(min=1)])
    body = TextAreaField("Body", [validators.Length(min=1)])
 
    class Meta:
        csrf = False