import sqlite3
#   CRUD bazy danych

class User:
    def __init__(self):
        self._conn = sqlite3.connect("Users_database.db")
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn


    @property
    def cursor(self):
        return


user = User()