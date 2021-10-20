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

    def __repr__(self):
        return f"User: ({self.email}, {self.password})" # Po wywołaniu zwraca login urzytkownika