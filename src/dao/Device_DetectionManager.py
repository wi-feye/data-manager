from src import db
from src.dao.manager import Manager
from src.models.Device_detection import Device_Detection

from sqlalchemy import and_
from sqlalchemy.orm import Query

class DeviceManager(Manager):

    @staticmethod
    def add(deviceDetection: Device_Detection):
        Manager.create(deviceDetection=deviceDetection)

    @staticmethod
    def get_all():
        deviceDetection_data = Manager.get_all()
        deviceDetection_data = [device_detection_dict(deviceDetection) for deviceDetection in deviceDetection_data]
        return deviceDetection_data

    @staticmethod
    def retrieve(self):
        """
        It should implemented by child
        :return:
        """
        pass  # pragma: no cover

def device_detection_dict(deviceDetection):
    return {
            'id': deviceDetection.id,
            'id_crowd' : deviceDetection.id_crowd,
            'id_workspace' : deviceDetection.id_workspace,
            'id_area' : deviceDetection.id_area,
            'mac_hash' : deviceDetection.mac_hash,
            'timestamp' : deviceDetection.timestamp,
            'x' : deviceDetection.x,
            'y' : deviceDetection.y,
            'state' : deviceDetection.state

    }