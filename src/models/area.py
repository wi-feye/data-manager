# from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
from sqlalchemy import tuple_


from src import db


class Area(db.Model):
    """Representation of areas."""

    # The name of the table that we explicitly set
    __tablename__ = "Area"

    # A list of fields to be serialized
    SERIALIZE_LIST = ["id", "id_building", "name", "color", "location", "description"]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_building = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    color = db.Column(db.String(20), nullable=True)
    location = db.Column(postgresql.ARRAY(db.Float(), dimensions=2), nullable=False) # deve essere array di coppie
    description = db.Column(db.String(150), nullable=True)

    def __init__(self, *args, **kw):
        super(Area, self).__init__(*args, **kw)

    def get_obj(self):
        area_obj = {
            "id": self.id,
            "id_building": self.id_building,
            "name": self.name,
            "color": self.color,
            "location": self.location,
            "description": self.description,
        }
        return area_obj

    def serialize(self) -> dict:
        return dict([(k, self.__getattribute__(k)) for k in self.SERIALIZE_LIST])
