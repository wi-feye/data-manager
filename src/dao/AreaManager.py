from src import db
from src.dao.manager import Manager
from src.models.area import Area

from sqlalchemy import and_
from sqlalchemy.orm import Query

import json

from sqlalchemy.orm import Session
from src import db 

class AreaManager(Manager):
    @staticmethod
    def get_all():
        areas = Area.query.all()
        areas = [area_dict(area) for area in areas]
        return areas

    @staticmethod
    def get_areas_by_building(id_building):
        areas = Area.query.filter_by(id_building=id_building).all()
        areas = [area_dict(area) for area in areas]
        return areas

    @staticmethod
    def add(area: Area):
        Manager.create(area=area)
        
    @staticmethod
    def delete_area_by_id(id_area):            
        Area.query.filter_by(id=id_area).delete()
        db.session.commit()
      
    @staticmethod
    def update_area_id(id, new_values):
        Area.query.filter_by(id=id).update(new_values)
        db.session.commit()
    
def area_dict(area):
    return {
        "id": area.id,
        "id_building": area.id_building,
        "name": area.name,
        "description": area.description,
        "color": area.color,
        "location": json.loads(area.location), # lista di liste di coordinate [x,y]
    }
