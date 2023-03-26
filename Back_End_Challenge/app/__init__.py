import os

from flask import Flask
from .config import Config
from flask_migrate import Migrate
from app.models import Reservation, db
from app.reservation_form import ReservationForm
from datetime import datetime
import pytz

app = Flask(__name__)
app.config.from_object(Config)
app.config['WTF_CSRF_ENABLED'] = False
# Note: I disabled CSRF because after reaching out to Steven
# I decided to focus the scope on just having the two routes work below without CSRF
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/reservation')
def get_all():
    # wrong because local time or not correct format
    #today = datetime.now()
    # utcToday = datetime.utcnow()

    # correct format
    now_utc = datetime.now(tz=pytz.utc)
    utcToday = now_utc.strftime('%Y-%m-%dT%H:%M:%SZ')

    reservations = Reservation.query.filter(
        Reservation.startTime
        >  utcToday
    ).all()
    # Note: I chose to return the dictionary with the key of Reservations to the list of all reservations
    # The status code build in returns 200 for the success of the 'GET' route
    return {'Reservations': [reservation.to_dict() for reservation in reservations]}


@app.route('/reservation', methods=['POST'])
def form():
    form = ReservationForm()

    if form.validate_order():

        new_reservation = Reservation()

        form.populate_obj(new_reservation)
        db.session.add(new_reservation)
        db.session.commit()
        return new_reservation.to_dict(), 201

    return {
        'message': 'Validation Error',
        "errors": form.errors,
        'statusCode': 400
    }, 400
