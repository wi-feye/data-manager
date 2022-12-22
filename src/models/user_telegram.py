from flask_sqlalchemy import SQLAlchemy
from src import db


class UserTelegram(db.Model):
    """Representation of building data."""

    # The name of the table that we explicitly set
    __tablename__ = "UserTelegram"

    # A list of fields to be serialized
    SERIALIZE_LIST = ["id_user", "chatid", "tmpcode", "gencode_timestamp", "enabled"]

    id_user = db.Column(db.Integer, primary_key=True, nullable=False)
    chatid = db.Column(db.Integer, nullable=True)
    tmpcode = db.Column(db.Integer, nullable=True)
    enabled = db.Column(db.Boolean, nullable=False, default=True)
    gencode_timestamp = db.Column(db.DateTime, nullable=True)

    def __init__(self, *args, **kw):
        super(UserTelegram, self).__init__(*args, **kw)

    def get_obj(self):
        building_obj = {
            "id_user": self.id_user,
            "chatid": self.chatid,
            "tmpcode": self.tmpcode,
            "enabled": self.enabled,
            "gencode_timestamp": self.gencode_timestamp,
        }
        return building_obj

    def serialize(self) -> dict:
        return dict([(k, self.__getattribute__(k)) for k in self.SERIALIZE_LIST])
