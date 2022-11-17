from src import db
from src.dao.manager import Manager
from src.models.Sniffer import Sniffer

from sqlalchemy import and_
from sqlalchemy.orm import Query


class SnifferManager(Manager):
    @staticmethod
    def add(sniffer: Sniffer):
        Manager.create(sniffer=sniffer)

    @staticmethod
    def get_all():
        sniffer_data = Sniffer.query.all()
        sniffer_data = [sniffer_dict(sniffer) for sniffer in sniffer_data]
        return sniffer_data


def sniffer_dict(sniffer):
    return {
        "id": sniffer.id,
        "id_zerynth": sniffer.id_zerynth,
        "id_building": sniffer.id_building,
        "name": sniffer.name,
        "x": sniffer.x,
        "y": sniffer.y,
    }
