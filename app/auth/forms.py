from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=1, max=35)])
    password = PasswordField("Password", [validators.Length(min=1, max=35)])
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=1, max=35)])
    username = StringField("Username", [validators.Length(min=1, max=35)])
    password = PasswordField("Password", [validators.Length(min=1, max=35)])
  
    class Meta:
        csrf = False