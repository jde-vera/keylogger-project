from . import db

class User(db.Model):
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def set_password(self, password):
        self.password=password