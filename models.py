from __init__ import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

class user(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class MostSelling(db.Model):
    __tablename__ = "mostselling"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(500), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    Nooftables = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f"MostSelling('{self.name}', '{self.email}', '{self.phone}', '{self.Nooftables}')"
        
