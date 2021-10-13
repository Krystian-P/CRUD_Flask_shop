from flask import Flask, render_template, request, redirect, url_for
from forms import *
from models import User
app = Flask(__name__)
app.config["SECRET_KEY"] = "Upikajej"


@app.route("/")
def welcome_page():     #Strona startowa
    return render_template("welcome.html")


@app.route("/login", methods=["GET", "POST"])
def login_page():       # Strona logowania
    loginform = LogIn()
    error = ""
    if request.method == 'POST' and loginform.validate_on_submit():
        user= User
        return redirect(url_for("user_profile_page"))
    return render_template("log-in.html", login_form=loginform)


@app.route("/sing-in", methods=["GET", "POST"])
def sing_in_page():     # Strona rejestracji
    form=SignIn()
    error=""
    if request.method == 'POST' and form.validate_on_submit():
        user= User
        return redirect(url_for("login_page"))
    return render_template("sing-in.html", signin_form=form)


@app.route("/user-profile.html", methods=["GET", "POST"])
def user_profile_page():       # Dane urzytkownika
    return render_template("user-profile.html")


if __name__ == "__main__":
    app.run(debug=True)
