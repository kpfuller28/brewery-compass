from flask import render_template, Blueprint, g, request, redirect, session
from .db import db
from .models import User, Saved
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
  session.clear()
  return redirect('/')

@routes.route('/search', methods=['POST'])
def search():
  search_term = request.form['search']
  return redirect(f'/dashboard?search={search_term}')

@routes.route('/addExplored', methods= ['POST'])
def addExplored():
  from .helpers import addSaved
  return addSaved(request.form['brewery'], 'explored')

@routes.route('/addRadar', methods=['POST'])
def addRadar():
  from .helpers import addSaved
  return addSaved(request.form['brewery'], 'radar')

@routes.route('/move', methods=['POST'])
def move():
  brewery = Saved.query.filter_by(brewery_id=request.form['id']).one()
  if request.form['type'] == 'explored':
    brewery.list_type = 'radar'
    brewery.rating = 0
    db.session.commit()
  else:
    brewery.list_type = 'explored'
    db.session.commit()
  return redirect('/dashboard')

@routes.route('/rate', methods=['POST'])
def rate():
  brewery = Saved.query.filter_by(brewery_id=request.form['id']).one()
  brewery.rating = request.form['rating']
  db.session.commit()
  return redirect('/dashboard')

@routes.route('/delete', methods=['POST'])
def delete():
  brewery = Saved.query.filter_by(brewery_id=request.form['id']).one()
  db.session.delete(brewery)
  db.session.commit()
  return redirect('/dashboard')

@routes.route('/dashboard')
def dashboard():
  search_terms = request.args.get('search')

  if search_terms != None:
    payload = {'query': search_terms}
    response = requests.get(g.url + '/search', params=payload)
    breweries = response.json() if response.status_code == 200 else []
    session['search'] = payload
  elif session.get('search'):
    response = requests.get(g.url + '/search', params=session['search'])
    breweries = response.json() if response.status_code == 200 else []
  else:
    breweries = None

  explored = Saved.query.filter_by(user_id=session['current_user']['id'], list_type='explored').order_by(Saved.rating.desc()).all()
  radar = Saved.query.filter_by(user_id=session['current_user']['id'], list_type='radar').all()
  if session.get('db_error'):
    error = session.pop('db_error')
  else:
    error = None


  return render_template('index.html', user=session['current_user'], breweries=breweries, explored=explored, radar=radar, error=error)

