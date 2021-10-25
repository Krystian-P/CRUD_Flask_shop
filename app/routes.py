from flask import Flask, render_template, request, redirect, url_for, flash
from app import app, db, bcrypt
from app.forms import LogIn, SignIn
from app.models import User
from flask_login import login_user,current_user, logout_user, login_required



@app.route("/")
def welcome_page():     #Strona startowa
    return render_template("welcome.html")


@app.route("/login", methods=["GET", "POST"])
def login_page():       # Strona logowania
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LogIn()
    if form.validate_on_submit():
        user = User.query.filter_by(email= form.Email.data).first()
        if user is not None and bcrypt.check_password_hash(user.password, form.Password.data):
            login_user(user, remember=form.Remember.data)
            return redirect(url_for('welcome_page'))
        else:
            flash('Login unsuccessful. Pleas check email and password', 'danger')
    return render_template("log-in.html", form=form)


@app.route("/sing-in", methods=["GET", "POST"])
def sing_in_page():     # Strona rejestracji
    if current_user.is_authenticated:
        return redirect(url_for('welcome_page'))
    form = SignIn()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.Password.data).decode('utf-8')
        user = User(username = form.Login.data, password=hashed_password, email=form.Email.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Your  account has been created!', 'success')
        return redirect(url_for('login_page'))
    return render_template("sing-in.html", title='Register', form=form)


@app.route("/user-profile.html", methods=["GET", "POST"])
def user_profile_page():       # Dane urzytkownika
    return render_template("user-profile.html")

if __name__ == '__main__':
    app.run(debug=True)