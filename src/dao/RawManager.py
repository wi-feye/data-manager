from src import db
from src.dao.manager import Manager
from src.models.raw import Raw

from sqlalchemy import and_
from sqlalchemy.orm import Query


class RawManager(Manager):
    @staticmethod
    def add(raw: Raw):
        Manager.create(raw=raw)

    @staticmethod
    def get_all():
        raw_data = Raw.query.all()
        raw_data = [raw_dict(raw) for raw in raw_data]
        return raw_data

    @staticmethod
    def get_raw_data_by_time_interval_by_building(id_building, start_time, end_time):
        raw_data = Raw.query.filter(and_(Raw.id_building == id_building, Raw.timestamp >= start_time, Raw.timestamp <= end_time)).all()
        # raw_data = [raw_dict(raw) for raw in raw_data]
        return raw_data

def raw_dict(raw):
    return {
        "id": raw.id,
        "timestamp": raw.timestamp,
        "mac": raw.mac,
        "rssi_1": raw.rssi_1,
        "rssi_2": raw.rssi_2,
        "rssi_3": raw.rssi_3,
    }
