from .models import Saved
from flask import session, redirect
from .db import db

def addSaved(brewery, list_type):
  import ast
  brewery = ast.literal_eval(brewery)
  try:
    saved_brewery = Saved(
        brewery_id=brewery['id'],
        user_id=session['current_user']['id'],
        name=brewery['name'],
        brewery_type=brewery['brewery_type'],
        address=brewery['address_1'],
        city=brewery['city'],
        state_province=brewery['state_province'],
        postal_code=brewery['postal_code'],
        country=brewery['country'],
        phone=brewery['phone'],
        website=brewery['website_url'],
        list_type=list_type
    )
    db.session.add(saved_brewery)
    db.session.commit()
  except Exception as error:
    db.session.rollback()
    print(f'Error adding brewery to {list_type.capitalize()} list: {error}')
    exists = Saved.query.filter_by(brewery_id=brewery['id']).one()
    session['db_error'] = f'Brewery already exists in {exists.list_type.capitalize()} list!'
    return redirect('/dashboard')

  print(f'Brewery added to {list_type.capitalize()}')
  return redirect('/dashboard')