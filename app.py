from app import create_app


# to do: refactor explored model to include all information needed.
# user rating, name, address, coordinates, url, etc?. this way the
# api doesn't need to be hit every time dashboard loads,
# instead i hit the db. Possibly add alembic to handle db migrations?
# might not be necessary though.

app = create_app()


if __name__ == '__main__':
  app.run(debug=True)




