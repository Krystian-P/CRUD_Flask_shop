from flask_wtf import FlaskForm
from wtforms.validators import *
from flask_login import current_user
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


class UpdateAccountForm(FlaskForm):
    Login = TextField("Login", validators=[DataRequired(), Length(min=5)])
    Email = TextField("Email", validators=[DataRequired(), Length(min=4), Email()])
    Submit = SubmitField('Update')

    def validate_username(self, Login):
        if Login.data != current_user.Login:
            user= User.query.filter_by(username=Login.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, Email):
        if Email.data != current_user.Email:
            email = Email.query.filter_by(email=Email.data).first()
            if email:
                raise ValidationError('That email is taken. Please choose a differnt one.')


class PostForm(FlaskForm):
    content = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Post')