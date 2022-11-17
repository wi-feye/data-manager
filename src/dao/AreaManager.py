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
        areas = Area.query.all()
        areas = [area_dict(area) for area in areas]
        return areas

def area_dict(area):
    return {
        'id': area.id,
        'id_building': area.id_building,
        'name': area.name,
        'color': area.color,
        'location': json.loads(area.location),
    }