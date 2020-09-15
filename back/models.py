from . import db

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    json_string = db.Column(db.String())

    def __init__(self, json_string):
        self.json_string = json_string

    def __repr__(self):
        return self.json_string

    def serialize(self):
        return {
            'id': self.id,
            'json_string': self.json_string
        }
