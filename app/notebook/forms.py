from flask_wtf import FlaskForm
from wtforms import StringField, validators

class NotebookForm(FlaskForm):
    title = StringField("Notebook title", validators=[validators.Length(min=1, max=100)])
    description = StringField("Description", validators=[validators.Length(min=1, max=280)])
 
    class Meta:
        csrf = False