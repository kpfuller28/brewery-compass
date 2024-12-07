from app import create_app, routes
from flask import g, current_app, request, redirect, session


app = create_app()

@app.before_request
def before_request():
  g.url = current_app.config['API_URL']
  if not session.get('loggedIn') and request.path != '/login':
    return redirect('/login')

app.register_blueprint(routes.routes)

if __name__ == '__main__':
  app.run(debug=True)




