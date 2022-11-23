from src import db
from src.dao.manager import Manager
from src.models.building import Building

from sqlalchemy import and_
from sqlalchemy.orm import Query


class BuildingManager(Manager):
    @staticmethod
    def add(building: Building):
        Manager.create(building=building)

    @staticmethod
    def update_by_id(id, new_values):
        Building.query.filter_by(id=id).update(new_values)

    @staticmethod
    def get_all():
        building_data = Building.query.all()
        building_data = [building_dict(building) for building in building_data]
        return building_data

    @staticmethod
    def get_building_by_id(id):
        building = Building.query.filter_by(id=id).first()
        return building_dict(building)

    @staticmethod
    def get_buildings_by_user(id_user):
        building_data = Building.query.filter_by(id_user=id_user).all()
        building_data = [building_dict(building) for building in building_data]
        return building_data


def building_dict(building):
    return {
        "id": building.id,
        "id_zerynth": building.id_zerynth,
        "id_user": building.id_user,
        "name": building.name,
        "lastupdate": building.lastupdate.isoformat(),
    }
