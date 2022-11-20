# from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.dialects.postgresql.array import ARRAY
from src import db


class Raw(db.Model):
    """Representation of raw data."""

    # The name of the table that we explicitly set
    __tablename__ = "Raw"

    # A list of fields to be serialized
    SERIALIZE_LIST = ["id", "timestamp", "mac_hash", "rssi_device"]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_building = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime)
    mac_hash = db.Column(db.String(100), nullable=True)
    rssi_device = db.Column(ARRAY(db.Integer, dimensions=2))


    def __init__(self, *args, **kw):
        super(Raw, self).__init__(*args, **kw)

    def get_obj(self):
        raw_obj = {
            "id": self.id,
            "timestamp": self.timestamp,
            "mac_hash": self.mac_hash,
            "rssi_device": self.rssi_device,
        }
        return raw_obj

    def serialize(self) -> dict:
        return dict([(k, self.__getattribute__(k)) for k in self.SERIALIZE_LIST])
