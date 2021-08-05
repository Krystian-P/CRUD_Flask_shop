from app import db
# moduł do wprowadzania zmian w strukturze bazy danech

class Users(db.Model):      # baza danych przechowyje dane każdego z urztkowników, hasło będzie zakodowane
    id= db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(40), index=True, unique=True)
    password = db.Column(db.String(40), index=True, unique=True)
    email= db.Column(db.String(50), index=True, unique=True)

    def __str__(self):
        return f"User: {self.login}" # Po wywołaniu zwraca login urzytkownika