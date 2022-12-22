from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from src import db


class Building(db.Model):
    """Representation of building data."""

    # The name of the table that we explicitly set
    __tablename__ = "Building"

    # A list of fields to be serialized
    SERIALIZE_LIST = ["id", "id_zerynth", "id_user", "name", "lastupdate", "open_time", "close_time", "last_tg_notification"]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_zerynth = db.Column(db.String(20), nullable=False)
    id_user = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    lastupdate = db.Column(db.DateTime, nullable=False)
    open_time = db.Column(db.DateTime, nullable=True)
    close_time = db.Column(db.DateTime, nullable=True)
    last_tg_notification = db.Column(db.DateTime, default=datetime(1970, 1, 1))

    def __init__(self, *args, **kw):
        super(Building, self).__init__(*args, **kw)

    def get_obj(self):
        building_obj = {
            "id": self.id,
            "id_zerynth": self.id_zerynth,
            "id_user": self.id_user,
            "name": self.name,
            "lastupdate": self.lastupdate,
            "open_time" : self.open_time,
            "close_time": self.close_time,
            "last_tg_notification": self.last_tg_notification
        }
        return building_obj

    def serialize(self) -> dict:
        return dict([(k, self.__getattribute__(k)) for k in self.SERIALIZE_LIST])
