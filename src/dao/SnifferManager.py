from src import db
from src.dao.manager import Manager
from src.models.sniffer import Sniffer

from sqlalchemy import and_
from sqlalchemy.orm import Query
from sqlalchemy.orm import Session

from src import db 

class SnifferManager(Manager):
    @staticmethod
    def add(sniffer: Sniffer):
        Manager.create(sniffer=sniffer)

    @staticmethod
    def get_all():
        sniffer_data = Sniffer.query.all()
        sniffer_data = [sniffer_dict(sniffer) for sniffer in sniffer_data]
        return sniffer_data

    @staticmethod
    def get_sniffers_by_building(id_building):
        sniffer_data = Sniffer.query.filter_by(id_building=id_building).all()
        sniffer_data = [sniffer_dict(sniffer) for sniffer in sniffer_data]
        return sniffer_data

    @staticmethod
    def delete_sniffer_by_id(id_sniffer):            
        Sniffer.query.filter_by(id=id_sniffer).delete()
        db.session.commit()

    @staticmethod
    def get_sniffer_by_id(id):
        sniffer = Sniffer.query.filter_by(id=id).first()
        return sniffer_dict(sniffer)

    @staticmethod
    def update_by_id(id, new_values):
        Sniffer.query.filter_by(id=id).update(new_values)
        db.session.commit()

def sniffer_dict(sniffer):
    return {
        "id": sniffer.id,
        "id_zerynth": sniffer.id_zerynth,
        "id_building": sniffer.id_building,
        "name": sniffer.name,
        "x": sniffer.x,
        "y": sniffer.y,
        "last_tg_notification": sniffer.last_tg_notification.isoformat()
    }
