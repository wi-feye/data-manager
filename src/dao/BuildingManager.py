from src import db
from src.dao.manager import Manager
from src.models.building import Building

from sqlalchemy import and_
from sqlalchemy.orm import Query
from sqlalchemy.orm import Session

from src import db 
from datetime import datetime


class BuildingManager(Manager):
    @staticmethod
    def add(building: Building):
        Manager.create(building=building)

    @staticmethod
    def update_by_id(id, new_values):
        Building.query.filter_by(id=id).update(new_values)
        db.session.commit()
        
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

    @staticmethod
    def delete_building_by_id(id_building):            
        Building.query.filter_by(id=id_building).delete()
        db.session.commit()
      
    @staticmethod
    def is_open_now(id_building):
        building = Building.query.filter_by(id=id_building).first()
        if building is None:
            return False
        open = (
            building.open_time.time()
            <= datetime.now().time()
            <= building.close_time.time()
        )
        return open

    @staticmethod
    def is_open_by_time(id_building, time):
        building = Building.query.filter_by(id=id_building).first()
        if building is None:
            return False
        open = building.open_time.time() <= time.time() <= building.close_time.time()
        return open


def building_dict(building):
    return {
        "id": building.id,
        "id_zerynth": building.id_zerynth,
        "id_user": building.id_user,
        "name": building.name,
        "lastupdate": building.lastupdate.isoformat(),
        "open_time": str(building.open_time.time()),
        "close_time": str(building.close_time.time()),
        "last_tg_notification": None if building.last_tg_notification is None else building.last_tg_notification.isoformat(),
    }
