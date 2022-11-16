from src import db
from src.dao.manager import Manager
from src.models.crowd import Crowd

from sqlalchemy import and_
from sqlalchemy.orm import Query

class CrowdManager(Manager):

    @staticmethod
    def add(crowd: Crowd):
        Manager.create(crowd=crowd)

    @staticmethod
    def get_all():
        _data = Manager.get_all()
        crowd_data = [crowd_dict(crowd) for crowd in crowd_data]
        return crowd_data

    @staticmethod
    def retrieve(self):
        """
        It should implemented by child
        :return:
        """
        pass  # pragma: no cover

def crowd_dict(crowd):
    return {
        'id': crowd.id,
        'timestamp': crowd.timestamp,
        'duration': crowd.mac,
    }