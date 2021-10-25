from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):      # baza danych przechowyje dane każdego z urztkowników, hasło będzie zakodowane
    id= db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(40), unique=True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    email= db.Column(db.String(50), unique=True, nullable = False)
    review=db.relationship('Review', backref='author', lazy=True)

    def __repr__(self):
        return f"User: ({self.email}, {self.password})" # Po wywołaniu zwraca login urzytkownika

class Review(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    post_date=db.Column(db.Date, default=datetime.utcnow())
    content=db.Column(db.Text, nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Review:('{self.post_date}')"
