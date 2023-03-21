from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Reservation(db.Model):
    __tablename__ = 'reservation'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50))
    event = db.Column(db.String(255))
    startTime = db.Column(db.String(255))
    endTime = db.Column(db.String(255))

    def to_dict(self):
      return {
        'id': self.id,
        'user':self.user,
        'event': self.event,
        'startTime': self.startTime,
        'endTime': self.endTime
      }
