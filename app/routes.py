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
  payload = {'by_city': 'san_diego', 'per_page': '3'}
  test = requests.get(g.url, params=payload)
  print(test.text)
  return render_template('index.html')

