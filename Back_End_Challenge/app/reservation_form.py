from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime
from app.models import Reservation


def valid_startTime(form, field):
    startTime = datetime.strptime(field.data,"%Y-%m-%dT%H:%M:%SZ")
    current=datetime.now()
    #datetime.now() is automatically local time
    if startTime<current:
        raise ValidationError('Start time can not be in the past.')

def valid_endTime(form, field):
    endTime = datetime.strptime(field.data,"%Y-%m-%dT%H:%M:%SZ")
    current=datetime.now()
    if endTime<current:
        raise ValidationError('End time can not be in the past.')

class ReservationForm(FlaskForm):
    user = StringField('user', validators=[DataRequired()])
    event = StringField('event', validators=[DataRequired()])
    startTime = StringField('startTime', validators=[DataRequired(), valid_startTime])
    endTime = StringField('endTime', validators=[DataRequired(), valid_endTime])


    def validate_order(self, **kwargs):
        # Standard validators
        rv = FlaskForm.validate(self)
        # Ensure all standard validators are met
        if rv:
            # Ensure end date >= start date
            startTime = datetime.strptime(self.startTime.data,"%Y-%m-%dT%H:%M:%SZ")
            endTime = datetime.strptime(self.endTime.data,"%Y-%m-%dT%H:%M:%SZ")
            if startTime >= endTime:
                self.endTime.errors.append('End time must be after the start time.')
                return False
            allReservations = Reservation.query.all()
            for res in allReservations:
                oneRes = res.to_dict()
                oneResStartString = str(oneRes['startTime'])
                #should convert to local time, then compared to time the user submitted in their local time
                compareStartTime = datetime.strptime(oneResStartString,"%Y-%m-%dT%H:%M:%SZ")
                oneResEndString = str(oneRes['endTime'])
                compareEndTime = datetime.strptime(oneResEndString,"%Y-%m-%dT%H:%M:%SZ")
                if startTime <= compareStartTime and endTime >= compareEndTime:
                    self.endTime.errors.append('This user already has an event completely overlapping with the specified time block')
                    return False
                if startTime > compareStartTime and endTime < compareEndTime:
                    self.endTime.errors.append('This user already has an event that starts before and continues to after this time block')
                    return False
                if startTime <= compareStartTime and endTime > compareStartTime:
                    self.endTime.errors.append('This user already has an event overlapping with the start time, but not the end time')
                    return False
                if endTime >= compareEndTime and startTime > compareEndTime:
                    self.endTime.errors.append('This user already has an event overlapping with the end time, but not the start time')
                    return False

            return True
        return False
