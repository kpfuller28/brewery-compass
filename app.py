from app import create_app, routes
from app.db import db
from flask import g, current_app, request, redirect, session

# to do: refactor explored model to include all information needed.
# user rating, name, address, coordinates, url, etc?. this way the
# api doesn't need to be hit every time dashboard loads,
# instead i hit the db. Possibly add alembic to handle db migrations?
# might not be necessary though.

app = create_app()
with app.app_context():
  from app.models import User
  db.create_all()

@app.before_request
def before_request():
  g.url = current_app.config['API_URL']
  if not session.get('loggedIn') and (request.path != '/login' and request.path != '/register'):
    return redirect('/login')

app.register_blueprint(routes.routes)

if __name__ == '__main__':
  app.run(debug=True)




