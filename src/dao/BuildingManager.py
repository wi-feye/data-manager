from src import db
from src.dao.manager import Manager
from src.models.Building import Building

from sqlalchemy import and_
from sqlalchemy.orm import Query


class BuildingManager(Manager):
    @staticmethod
    def add(building: Building):
        Manager.create(building=building)

    @staticmethod
    def get_all():
        building_data = Building.query.all()
        building_data = [building_dict(building) for building in building_data]
        return building_data


def building_dict(building):
    return {
        "id": building.id,
        "id_zerynth": building.id_zerynth,
        "id_user": building.id_user,
        "name": building.name,
    }
