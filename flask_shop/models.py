from flask_shop import db, login_manager
from flask_login import UserMixin
# moduł do wprowadzania zmian w strukturze bazy danech

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):      # baza danych przechowyje dane każdego z urztkowników, hasło będzie zakodowane
    id= db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(40), index=True, unique=True)
    password = db.Column(db.String(40), index=True, unique=True)
    email= db.Column(db.String(50), index=True, unique=True)

    def __repr__(self):
        return f"User: ({self.login},{self.email})" # Po wywołaniu zwraca login urzytkownika