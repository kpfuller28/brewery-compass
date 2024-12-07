import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

def create_app():

  app = Flask(__name__)
  app.secret_key = os.getenv('SECRET_KEY')
  app.config['API_URL'] = os.getenv('API_URL')
  return app