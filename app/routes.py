from flask import render_template, Blueprint, g, request, redirect, session
from .db import db
from .models import User, Explored, Radar
import requests


routes = Blueprint('routes', __name__)


@routes.route('/')
def index():
  return redirect('/dashboard')

@routes.route('/register', methods=['GET', 'POST'])
def register():
    try:
      new_user = User(username=request.form['username'], password=request.form['password'])
      db.session.add(new_user)
      db.session.commit()
      session['loggedIn'] = True
      session['current_user'] = {'username': new_user.username, 'id': new_user.id}
    except Exception as error:
      print('----------------------------------------')
      print(error)
      print('----------------------------------------')
      register_error ='There was a problem registering: Username unavailable.'
      return render_template('login.html', register_error=register_error)
    return redirect('/dashboard')

@routes.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    try:
      user = User.query.filter_by(username=username, password=password).one()
    except:
      login_error = 'Login information was incorrect. Please try again or register a new account.'
      return render_template('login.html', login_error=login_error)
    session['loggedIn'] = True
    session['current_user'] = {'username': user.username, 'id': user.id}
    return redirect('/dashboard')
  return render_template('login.html')

@routes.route('/logout', methods=['POST'])
def logout():
  session['loggedIn'] =  False
  return redirect('/')

@routes.route('/search', methods=['POST'])
def search():
  search_term = request.form['search']
  return redirect(f'/dashboard?search={search_term}')

@routes.route('/addExplored', methods= ['POST'])
def addExplored():
  try:
    explored_brewery = Explored(brewery_id=request.form['id'], user_id=session['current_user']['id'])
    db.session.add(explored_brewery)
    db.session.commit()
  except Exception as error:
    print(f'Error adding brewery to Explored list: {error}')
    return redirect('/dashboard')

  print('Brewery added to Explored')
  return redirect(f'/dashboard')


@routes.route('/addRadar', methods=['POST'])
def addRadar():
  print('Brewery added to Your Radar')
  return redirect('/dashboard')

@routes.route('/dashboard')
def dashboard():
  search_terms = request.args.get('search')
  breweries = []
  radar = []

  if search_terms:
    payload = {'query': search_terms}
    response = requests.get(g.url + '/search', params=payload)
    breweries = response.json() if response.status_code == 200 else []
  else:
    explored = []
    explored_results = Explored.query.filter_by(user_id=session['current_user']['id']).all()
    for brewery in explored_results:
      r = requests.get(g.url + '/' + brewery.brewery_id)
      explored.append(r.json()) if r.status_code == 200 else []
      print(explored)
  return render_template('index.html', user=session['current_user'], breweries=breweries, explored=explored)

