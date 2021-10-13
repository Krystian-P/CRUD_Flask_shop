from flask_wtf import FlaskForm
from wtforms.validators import *
from wtforms import *
from email_validator import validate_email

class LogIn(FlaskForm):
    #formularz logowania
    Login = TextField("Login", validators=[DataRequired()])
    Password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('LogIn')


class SignIn(FlaskForm):
    #fromularz rejestracji
    Login = TextField("Login", validators=[DataRequired(), Length(min=5)])
    Password = PasswordField("Password", validators=[DataRequired(), Length(min=6), EqualTo('Repeat_Password', message='Passwords must match')])
    Repeat_Password = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo('Password', message='Passwords must match')])
    Email = TextField("Email", validators=[DataRequired(), Length(min=4), Email()])
    submit = SubmitField('SignIn')