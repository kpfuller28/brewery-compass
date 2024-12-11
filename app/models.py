from .db import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(80))
  saved = db.relationship('Saved', backref='user')

class Saved(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  brewery_id = db.Column(db.String(80), unique=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  name = db.Column(db.String(80))
  brewery_type = db.Column(db.String(80))
  address = db.Column(db.String(80))
  city = db.Column(db.String(80))
  state_province = db.Column(db.String(80))
  postal_code = db.Column(db.String(80))
  country = db.Column(db.String(80))
  phone = db.Column(db.String(80))
  website = db.Column(db.String(80))
  list_type = db.Column(db.String(20))
  rating = db.Column(db.Integer, default=0)
