from flask_sqlalchemy import SQLAlchemy
from src import db

class Device_Detection(db.Model):
    """Representation of Device Detection data."""

    # The name of the table that we explicitly set
    __tablename__ = 'Device_Detection'

    # A list of fields to be serialized
    SERIALIZE_LIST = ['id', 'id_crowd', 'id_workspace', 'id_area', 'mac_hash', 'timestamp', 'x', 'y', 'state']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_crowd = db.Column(db.Integer, nullable=True)
    id_workspace = db.Column(db.Integer, nullable=False)
    id_area = db.Column(db.Integer, nullable=True)
    mac_hash = db.Column(db.String(32), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    x = db.Column(db.Integer, nullable=True)
    y = db.Column(db.Integer, nullable=True)
    state = db.Column(db.String(20), nullable=False, default='raw')
    #todo: 

    def __init__(self, *args, **kw):
        super(Device_Detection, self).__init__(*args, **kw)
    
    def get_obj(self):
        message_obj = {
            'id': self.id,
            'id_crowd' : self.id_crowd,
            'id_workspace' : self.id_workspace,
            'id_area' : self.id_area,
            'mac_hash' : self.mac_hash,
            'timestamp' : self.timestamp,
            'x' : self.x,
            'y' : self.y,
            'state' : self.state
        }
        return message_obj

    def serialize(self) -> dict:
        return dict([(k, self.__getattribute__(k)) for k in self.SERIALIZE_LIST])