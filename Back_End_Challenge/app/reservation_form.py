from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime
from app.models import Reservation
import pytz


# need to convert startTime to same format as now_utc
def valid_startTime(form, field):
    startTime = datetime.strptime(field.data, "%Y-%m-%dT%H:%M:%SZ")
    startTime_utc = pytz.utc.localize(startTime) # add timezone information
    now_utc = datetime.now(tz=pytz.utc)
    if startTime_utc < now_utc:
        raise ValidationError('Start time can not be in the past for local time.')


# validation the endTime is after the current time was not in the instructions, but I added it
def valid_endTime(form, field):
    endTime = datetime.strptime(field.data, "%Y-%m-%dT%H:%M:%SZ")
    endTime_utc = pytz.utc.localize(endTime)
    now_utc = datetime.now(tz=pytz.utc)
    if endTime_utc < now_utc:
        raise ValidationError('End time can not be in the past for local time.')


class ReservationForm(FlaskForm):
    user = StringField('user', validators=[DataRequired()])
    event = StringField('event', validators=[DataRequired()])
    startTime = StringField('startTime', validators=[
                            DataRequired(), valid_startTime])
    endTime = StringField('endTime', validators=[
                          DataRequired(), valid_endTime])

    def validate_order(self):
        # Standard validators
        rv = FlaskForm.validate(self)
        # Ensure all standard validators are met
        if rv:
            # Ensure end date >= start date, was not in the instructions but I added it
            startTime = datetime.strptime(
                self.startTime.data, "%Y-%m-%dT%H:%M:%SZ")
            endTime = datetime.strptime(
                self.endTime.data, "%Y-%m-%dT%H:%M:%SZ")
            if startTime > endTime:
                self.endTime.errors.append(
                    'End time must be after the start time.')
                return False
            allReservations = Reservation.query.all()
            for res in allReservations:

                oneRes = res.to_dict()
                oneResStartString = str(oneRes['startTime'])
                compareStartTime = datetime.strptime(
                    oneResStartString, "%Y-%m-%dT%H:%M:%SZ")
                oneResEndString = str(oneRes['endTime'])
                compareEndTime = datetime.strptime(
                    oneResEndString, "%Y-%m-%dT%H:%M:%SZ")

                compareUser = oneRes['user']
                #print('compareUser', compareUser, 'self.user', self.user.data)
                # I decided to give very clear feedback to the user for them to try a better reservation time
                if compareUser == self.user.data:
                    if startTime == compareStartTime and endTime == compareEndTime:
                        self.endTime.errors.append(
                            f'''{compareUser} already has an event with that exact time block new: {startTime} == cur: {compareStartTime} and new: {endTime}  == cur: {compareEndTime} ''')
                        return False
                    if startTime < compareStartTime and endTime > compareEndTime:
                        self.endTime.errors.append(
                            f'''{compareUser} already has an event that starts before and continues to after this time block new: {startTime}  < cur: {compareStartTime} and new: {endTime}  > cur: {compareEndTime} ''')
                        return False
                    if startTime <= compareStartTime and endTime > compareStartTime:
                        self.endTime.errors.append(
                            f'''{compareUser} already has an event overlapping with the start time, but not the end time new: {startTime}  <= cur: {compareStartTime} and new: {endTime}  > cur: {compareStartTime} ''')
                        return False
                    if endTime >= compareEndTime and startTime < compareEndTime:
                        self.endTime.errors.append(
                            f'''{compareUser} already has an event overlapping with the end time, but not the start time  new: {endTime}  >= cur: {compareEndTime} and new: {startTime}  < cur: {compareEndTime} ''')
                        return False

            return True
        return False
