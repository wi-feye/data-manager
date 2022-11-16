from src import db
from src.dao.manager import Manager
from src.models.sniffer import Sniffer

from sqlalchemy import and_
from sqlalchemy.orm import Query

class SnifferManager(Manager):

    @staticmethod
    def add(sniffer: Sniffer):
        Manager.create(sniffer=sniffer)

    @staticmethod
    def get_all():
        sniffer_data = Manager.get_all()
        sniffer_data = [sniffer_dict(sniffer) for sniffer in sniffer_data]
        return sniffer_data

    @staticmethod
    def retrieve(self):
        """
        It should implemented by child
        :return:
        """
        pass  # pragma: no cover

def sniffer_dict(sniffer):
    return {
        'id': sniffer.id,
        'id_zerynth': sniffer.id_zerynth,
        'id_building': sniffer.id_building,
        'name': sniffer.name,
        'location': sniffer.location
    }