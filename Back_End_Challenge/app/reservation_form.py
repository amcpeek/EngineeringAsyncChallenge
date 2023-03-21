from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ReservationForm(FlaskForm):
    user = StringField('user', validators=[DataRequired()])
    event = StringField('event', validators=[DataRequired()])
    startTime = StringField('startTime', validators=[DataRequired()])
    endTime = StringField('endTime', validators=[DataRequired()])


    # submit = SubmitField("Not sure needed")
