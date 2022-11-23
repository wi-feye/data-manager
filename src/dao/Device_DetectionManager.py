from src import db
from src.dao.manager import Manager
from src.models.position_detection import Device_Detection

from sqlalchemy import and_
from sqlalchemy.orm import Query


class DeviceManager(Manager):
    @staticmethod
    def add(deviceDetection: Device_Detection):
        Manager.create(deviceDetection=deviceDetection)

    @staticmethod
    def get_all():
        deviceDetection_data = Device_Detection.query.all()
        deviceDetection_data = [
            device_detection_dict(deviceDetection)
            for deviceDetection in deviceDetection_data
        ]
        return deviceDetection_data

    @staticmethod
    def get_by_id(id):
        deviceDetection_data = Device_Detection.query.filter_by(id=id).first()
        return device_detection_dict(deviceDetection_data)

    @staticmethod
    def get_data(id_building, start_time=None, end_time=None, id_area=None):
        filters = [Device_Detection.id_building == id_building]
        if start_time is not None:
            filters.append(Device_Detection.timestamp >= start_time)
        if end_time is not None:
            filters.append(Device_Detection.timestamp <= end_time)
        if id_area is not None:
            filters.append(Device_Detection.id_area == id_area)
        data = Device_Detection.query.filter(and_(*filters)).all()
        _data = [device_detection_dict(raw) for raw in data]
        return _data


def device_detection_dict(deviceDetection):
    return {
        "id": deviceDetection.id,
        "id_area": deviceDetection.id_area,
        "id_building": deviceDetection.id_building,
        "timestamp": deviceDetection.timestamp.isoformat(),
        "x": deviceDetection.x,
        "y": deviceDetection.y,
    }
