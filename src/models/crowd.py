# from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from src import db


class Crowd(db.Model):
    """Representation of Crowd data."""

    # The name of the table that we explicitly set
    __tablename__ = "Crowd"

    # A list of fields to be serialized
    SERIALIZE_LIST = ["id", "timestamp", "duration"]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime)
    duration = db.Column(db.Integer, nullable=False)

    def __init__(self, *args, **kw):
        super(Crowd, self).__init__(*args, **kw)

    def get_obj(self):
        message_obj = {
            "id": self.id,
            "timestamp": self.timestamp,
            "duration": self.duration,
        }
        return message_obj

    def serialize(self) -> dict:
        return dict([(k, self.__getattribute__(k)) for k in self.SERIALIZE_LIST])
