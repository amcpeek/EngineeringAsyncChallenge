download
pipenv install Flask
pipenv install python-dotenv
pipenv install Flask-WTF
pipenv install wtforms
pipenv install SQLAlchemy Flask-SQLAlchemy
pipenv install alembic Flask-Migrate


use the .env.example to create the .env

pipenv shell
pipenv run flask db init


pipenv run flask db migrate -m "create reservations table"
pipenv run flask db upgrade
