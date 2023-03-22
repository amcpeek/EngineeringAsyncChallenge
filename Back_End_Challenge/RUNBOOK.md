# Back End Challenge:

# Instructions:

## Install the following:

- Flask python-dotenv Flask-WTF wtforms SQLAlchemy Flask-SQLAlchemy alembic Flask-Migrate
- They are listed in the Pipefile
- In the terminal to install all of them, write:
- pipenv install
- use the .env.example to create the .env, because that is blocked when uploading to Github by the .gitignore file

## Enter the shell:

- In the terminal, write:
- pipenv shell

## Set up the database:

- In the terminal, write:
- flask db init
- flask db migrate -m "set up"
- flask db upgrade

## Start the server:

- flask run

# Notes:

- I decided not to seed the database
- In the instructions it request you add the reservation to "their profile" for a user.
  - A POST endpoint at `/reservation` where a user submits a JSON request to add an event reservation to their profile
  - A GET endpoint at `/reservation` where a user gets all future event reservations in their profile
- Given the following:

* the route does not have a parameter for the user id
* the JSON object only has the "user" as a string name and not a userId connecting to another table

- I could create authorization routes and a user table that would verify the user is logged in and return reservations based on their login information, but I checked in with Stephen Brewer and confirmed that is out of the scope of this assignment
