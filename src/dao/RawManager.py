from src import db
from src.dao.manager import Manager
from src.models.Raw import Raw

from sqlalchemy import and_
from sqlalchemy.orm import Query

class RawManager(Manager):

    @staticmethod
    def add(raw: Raw):
        Manager.create(raw=raw)

    @staticmethod
    def get_all():
        raw_data = Manager.get_all()
        raw_data = [raw_dict(raw) for raw in raw_data]
        return raw_data

    @staticmethod
    def retrieve(self):
        """
        It should implemented by child
        :return:
        """
        pass  # pragma: no cover

def raw_dict(raw):
    return {
        'id': raw.id,
        'timestamp': raw.timestamp,
        'mac': raw.mac,
        'rssi_1': raw.rssi_1,
        'rssi_2': raw.rssi_2,
        'rssi_3': raw.rssi_3
    }