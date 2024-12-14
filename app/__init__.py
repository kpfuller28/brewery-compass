import os
from flask import Flask, g, current_app, request, redirect, session
from dotenv import load_dotenv
from .db import db


load_dotenv()


def create_app():

  app = Flask(__name__)
  app.secret_key = os.getenv('SECRET_KEY')
  app.config['API_URL'] = os.getenv('API_URL')
  app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
  print('--------------------------------------------')
  print(os.name)
  print(os.getenv('DB_URI'))
  print('--------------------------------------------')
  db.init_app(app)

  with app.app_context():
    from app.models import User, Saved
    db.create_all()

  @app.before_request
  def before_request():
    g.url = current_app.config['API_URL']
    if not session.get('loggedIn') and (request.path != '/login' and request.path != '/register'):
      return redirect('/login')

  from app import routes
  app.register_blueprint(routes.routes)
  return app