from src import db
from src.models.raw import Raw
from src.models.area import Area

class Manager(object):

    db_session = db.session

    @staticmethod
    def check_none(**kwargs):
        for name, arg in zip(kwargs.keys(), kwargs.values()):
            if arg is None:
                raise ValueError('You can\'t set %s argument to None' % name)

    @staticmethod
    def create(**kwargs):
        Manager.check_none(**kwargs)
        for bean in kwargs.values():
            db.session.add(bean)

        db.session.commit()

    @staticmethod
    def update(**kwargs):
        Manager.check_none(**kwargs)
        db.session.commit()

    @staticmethod
    def delete(**kwargs):
        Manager.check_none(**kwargs)

        for bean in kwargs.values():
            db.session.delete(bean)
        db.session.commit()