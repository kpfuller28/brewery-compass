from .db import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(80))
  explored_list = db.relationship('Explored', backref='user')
  radar_list = db.relationship('Radar', backref='user')

class Explored(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  brewery_id = db.Column(db.String(80))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Radar(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  brewery_id = db.Column(db.String(80))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))