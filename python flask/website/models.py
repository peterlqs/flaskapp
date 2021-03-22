from . import db #. mean everything
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now()) #func get current datetime
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #1 to many relationship ex : 1 user has many notes

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True) #primary_key : unique identify
    email = db.Column(db.String(150),unique=True) #unique=True : no user can have that email that alr existed
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
