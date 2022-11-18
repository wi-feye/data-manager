from flask_sqlalchemy import SQLAlchemy
from src import db


class Sniffer(db.Model):
    """Representation of sniffers."""

    # The name of the table that we explicitly set
    __tablename__ = "Sniffer"

    # A list of fields to be serialized
    SERIALIZE_LIST = ["id", "id_zerynth", "id_building", "name", "x", "y"]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_zerynth = db.Column(db.String(20), nullable=False)
    id_building = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    x = db.Column(db.Float, nullable=False)
    y = db.Column(db.Float, nullable=False)

    def __init__(self, *args, **kw):
        super(Sniffer, self).__init__(*args, **kw)

    def get_obj(self):
        sniffer_obj = {
            "id": self.id,
            "id_zerynth": self.id_zerynth,
            "id_building": self.id_building,
            "name": self.name,
            "x": self.x,
            "y": self.y,
        }
        return sniffer_obj

    def serialize(self) -> dict:
        return dict([(k, self.__getattribute__(k)) for k in self.SERIALIZE_LIST])
