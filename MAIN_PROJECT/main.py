from flask import Flask, render_template, request
from forms import *
from models import User
app = Flask(__name__)
app.config["SECRET_KEY"] = "kokokokkok"


@app.route("/")
def welcome_page():
    return render_template("welcome.html")


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form=LogIn()
    error=""
    return render_template("log-in.html", login_form=form)


@app.route("/sing-in", methods=["GET", "POST"])
def sing_in_page():
    form=SignIn()
    error=""
    if request.method == 'POST' and form.validate():
        user= User
    return render_template("sing-in.html", signin_form=form)


@app.route("/user-profile.html", methods=["GET", "POST"])
def user_profile_page():
    return render_template("user-profile.html")


if __name__ == "__main__":
    app.run(debug=True)
