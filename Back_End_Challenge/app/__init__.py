import os

from flask import Flask, jsonify
from .config import Config
from flask_migrate import Migrate
from app.models import Reservation, db
from app.reservation_form import ReservationForm
# from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)
app.config['WTF_CSRF_ENABLED'] = False
db.init_app(app)
migrate = Migrate(app, db)
# csrf = CSRFProtect(app)


@app.route('/reservation')
def get_all():
    return {'Reservations': [reservation.to_dict() for reservation in Reservation.query.all()]}



@app.route('/reservation', methods=['POST'])
def form():
    form = ReservationForm()

    if form.validate_on_submit():

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

        # new_reservation=Reservation()
     #   data = form.data

            # user=data['user'],
            #                           event=data['event'],
            #                           startTime=['startTime'],
            #                           endTime=data['endTime'])

            # if form.validate_on_submit():
    #     data = form.data
    #     new_reservation = Reservation(user=data['user'],
    #                                   event=data['event'],
    #                                   startTime=['startTime'],
    #                                   endTime=data['endTime'])
    #     db.session.add(new_reservation)
    #     db.session.commit()
