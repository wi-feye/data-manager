from flask_sqlalchemy import SQLAlchemy
from src import db


class Device_Detection(db.Model):
    """Representation of Device Detection data."""

    # The name of the table that we explicitly set
    __tablename__ = "Device_Detection"

    # A list of fields to be serialized
    SERIALIZE_LIST = [
        "id",
        "id_building",
        "id_area",
        "x",
        "y",
        "id_crowd",
    ]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_building = db.Column(db.Integer, nullable=False)
    id_area = db.Column(db.Integer, nullable=True)
    x = db.Column(db.Float, nullable=True)
    y = db.Column(db.Float, nullable=True)
    id_crowd = db.Column(db.Integer, nullable=True)
    # todo:

    def __init__(self, *args, **kw):
        super(Device_Detection, self).__init__(*args, **kw)

    def get_obj(self):
        dev_det_obj = {
            "id": self.id,
            "id_crowd": self.id_crowd,
            "id_building": self.id_building,
            "id_area": self.id_area,
            "x": self.x,
            "y": self.y,
            "id_crowd": self.id_crowd,
        }
        return dev_det_obj

    def serialize(self) -> dict:
        return dict([(k, self.__getattribute__(k)) for k in self.SERIALIZE_LIST])
