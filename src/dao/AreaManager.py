from src import db
from src.dao.manager import Manager
from src.models.area import Area

from sqlalchemy import and_
from sqlalchemy.orm import Query

import json

class AreaManager(Manager):

    @staticmethod
    def add(area: Area):
        Manager.create(area=area)

    @staticmethod
    def get_all():
        area_data = Manager.get_all()
        area_data = [area_dict(raw) for raw in area_data]
        return area_data

    @staticmethod
    def retrieve(self):
        """
        It should implemented by child
        :return:
        """
        pass  # pragma: no cover

def area_dict(area):
    return {
        'id': area.id,
        'id_building': area.id_building,
        'name': area.name,
        'color': area.color,
        'location': json.loads(area.location),
    }