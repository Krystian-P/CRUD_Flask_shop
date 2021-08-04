from flask_wtf import FlaskForm
from wtforms.validators import *
from wtforms import *


class LogIn(FlaskForm):
    Login = TextField("Login", validators=[DataRequired()])
    Password = PasswordField("Password", validators=[DataRequired()])


class SignIn(FlaskForm):
    Login = TextField("Login", validators=[DataRequired(), Length(min=5)])
    Password = PasswordField("Password", validators=[DataRequired(), Length(min=6), EqualTo('Repeat_Password', message='Passwords must match')])
    Repeat_Password = PasswordField("Repeat Password", validators=[])
    Email = TextField("Email", validators=[DataRequired(), Length(min=4), Email()])
