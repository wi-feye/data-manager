#from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from src import db

class Raw(db.Model):
    """Representation of raw data."""

    # The name of the table that we explicitly set
    __tablename__ = 'Raw'

    # A list of fields to be serialized
    SERIALIZE_LIST = ['id', 'timestamp', 'mac', 'rssi_1', 'rssi_2', 'rssi_3']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime)
    mac = db.Column(db.Unicode(10), nullable=True)
    rssi_1 = db.Column(db.Integer, nullable=True)
    rssi_2 = db.Column(db.Integer, nullable=True)
    rssi_3 = db.Column(db.Integer, nullable=True)

    def __init__(self, *args, **kw):
        super(Raw, self).__init__(*args, **kw)
    
    def get_obj(self):
        message_obj = {
            'id': self.id,
            'timestamp': self.timestamp,
            'mac': self.mac,
            'rssi_1': self.rssi_1,
            'rssi_2': self.rssi_2,
            'rssi_3': self.rssi_3
        }
        return message_obj

    def serialize(self) -> dict:
        return dict([(k, self.__getattribute__(k)) for k in self.SERIALIZE_LIST])