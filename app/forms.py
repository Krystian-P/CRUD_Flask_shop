from flask_wtf import FlaskForm
from wtforms.validators import *
from wtforms import *
from app.models import User
from email_validator import validate_email

class LogIn(FlaskForm):
    #formularz logowania
    Email = TextField("Email", validators=[DataRequired(), Length(min=4), Email()])
    Password = PasswordField("Password", validators=[DataRequired()])
    Remember = BooleanField('Remember me')
    Submit = SubmitField('LogIn')


class SignIn(FlaskForm):
    #fromularz rejestracji
    Login = TextField("Login", validators=[DataRequired(), Length(min=5)])
    Password = PasswordField("Password", validators=[DataRequired(), Length(min=6), EqualTo('Repeat_Password', message='Passwords must match')])
    Repeat_Password = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo('Password', message='Passwords must match')])
    Email = TextField("Email", validators=[DataRequired(), Length(min=4), Email()])
    Submit = SubmitField('SignIn')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')