import os

from flask import Flask, jsonify
from .config import Config
from flask_migrate import Migrate
from app.models import Reservation, db
from app.reservation_form import ReservationForm
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
app.config['WTF_CSRF_ENABLED'] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/reservation')
def get_all():
    today = datetime.now()
    reservations = Reservation.query.filter(
        Reservation.startTime
        > today
    ).all()
    return {'Reservations': [reservation.to_dict() for reservation in reservations]}


@app.route('/reservation', methods=['POST'])
def form():
    form = ReservationForm()

    if form.validate_order():

        new_reservation = Reservation()



        form.populate_obj(new_reservation)
        db.session.add(new_reservation)
        db.session.commit()
        return new_reservation.to_dict(),201

    return {
        'message':'Validation Error',
        "errors":form.errors,
        'statusCode': 400
        },400
