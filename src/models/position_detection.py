from flask_sqlalchemy import SQLAlchemy
from src import db


class Device_Detection(db.Model):
    """Representation of Device Detection data."""

    # The name of the table that we explicitly set
    __tablename__ = "Device_Detection"

    # A list of fields to be serialized
    SERIALIZE_LIST = [
        "id",
        "id_area",
        "id_building"
        "timestamp"
        "x",
        "y",
    ]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_area = db.Column(db.Integer, nullable=True)
    id_building = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    x = db.Column(db.Float, nullable=True)
    y = db.Column(db.Float, nullable=True)

    def __init__(self, *args, **kw):
        super(Device_Detection, self).__init__(*args, **kw)

    def get_obj(self):
        dev_det_obj = {
            "id": self.id,
            "id_area": self.id_area,
            "id_building": self.id_building,
            "timestamp": self.timestamp.isoformat(),
            "x": self.x,
            "y": self.y,
        }
        return dev_det_obj

    def serialize(self) -> dict:
        return dict([(k, self.__getattribute__(k)) for k in self.SERIALIZE_LIST])
