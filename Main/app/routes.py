from flask import Flask, render_template, request, redirect, url_for, flash, abort
from app import app, db, bcrypt
from app.forms import LogIn, SignIn, PostForm, UpdateAccountForm
from app.models import User, Review, Vege_Review
from flask_login import login_user,current_user, logout_user, login_required



@app.route("/")
def welcome_page():     #Strona startowa
    return render_template("home.html")


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
        return redirect(url_for('home'))
    form = SignIn()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.Password.data).decode('utf-8')
        user = User(username = form.Login.data, password=hashed_password, email=form.Email.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Your  account has been created!', 'success')
        return redirect(url_for('login_page'))
    return render_template("sing-in.html", title='Register', form=form)


@app.route("/user-profile", methods=["GET", "POST"])
@login_required
def user_profile_page():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username=form.Login.data
        current_user.email=form.Email.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('user_profile_page'))
    elif request.method == 'GET':
        form.Login.data = current_user.username
        form.Email.data = current_user.email
    return render_template("user-profile.html", title='Account', form=form)


@app.route("/meat", methods=["GET", "POST"])
@login_required
def meat():       # Dane urzytkownika
    form=PostForm()
    if form.validate_on_submit():
        review = Review(content=form.content.data, author=current_user)
        db.session.add(review)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('meat'))
    review = Review.query.all()
    return render_template("meat.html", form=form, reviews=review)


@app.route("/vege", methods=["GET", "POST"])
@login_required
def vege():       # Dane urzytkownika
    form=PostForm()
    if form.validate_on_submit():
        vege_review = Vege_Review(content=form.content.data, author=current_user)
        db.session.add(vege_review)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('vege'))
    review = Vege_Review.query.all()
    return render_template("vege.html", form=form, reviews=review)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Vege_Review.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('vege'))
    elif request.method == 'GET':
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


if __name__ == '__main__':
    app.run(debug=True)