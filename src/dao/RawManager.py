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
    def get_raw_data_by_building(id_building):
        raw_data = Raw.query.filter_by(id_building=id_building).all()
        raw_data = [raw_dict(raw) for raw in raw_data]
        return raw_data

    @staticmethod
    def get_raw_data_by_time_interval_by_building(id_building, start_time, end_time):
        raw_data = Raw.query.filter(
            and_(
                Raw.id_building == id_building,
                Raw.timestamp >= start_time,
                Raw.timestamp <= end_time,
            )
        ).all()
        raw_data = [raw_dict(raw) for raw in raw_data]
        return raw_data

    @staticmethod
    def get_raw_data_by_building_start_time(id_building, start_time):
        raw_data = Raw.query.filter(
            and_(Raw.id_building == id_building, Raw.timestamp >= start_time)
        ).all()
        raw_data = [raw_dict(raw) for raw in raw_data]
        return raw_data


def raw_dict(raw):
    list_rssi = []
    for x in raw.rssi_device:
        json = {
            "id": x[0],
            "rssi": x[1]
        }
        list_rssi.append(json)
    return {
        "id": raw.id,
        "id_building": raw.id_building,
        "timestamp": raw.timestamp.isoformat(),
        "mac_hash": raw.mac_hash,
        "rssi_device": list_rssi,
    }
