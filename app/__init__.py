import os
from flask import Flask
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
  print(app.config['SQLALCHEMY_DATABASE_URI'])
  print('--------------------------------------------')
  db.init_app(app)
  return app