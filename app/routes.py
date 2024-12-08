from flask import render_template, Blueprint, g, request, redirect, session
import requests

routes = Blueprint('routes', __name__)


@routes.route('/')
def index():
  return redirect('/dashboard')

@routes.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    session['loggedIn'] = True
    return redirect('/')
  return render_template('login.html')

@routes.route('/logout', methods=['POST'])
def logout():
  session['loggedIn'] =  False
  return redirect('/')

@routes.route('/dashboard')
def dashboard():
  return render_template('index.html')

