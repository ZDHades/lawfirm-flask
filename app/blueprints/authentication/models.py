from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# creating a user class
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def hash_pass(self, origina_password):
        self.password = generate_password_hash(origina_password)

    def check_password(self, origina_password):
        return check_password_hash(self.password, origina_password)

    def __repr__(self):
        return f"<user: {self.first_name} {self.last_name}"


@login.user_loader
def login_user(id):
    return User.query.get(int(id))