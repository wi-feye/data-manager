from src import db
from src.dao.manager import Manager
from src.models.Raw import Raw

from sqlalchemy import and_
from sqlalchemy.orm import Query

class RawManager(Manager):

    @staticmethod
    def add(raw : Raw):
        Manager.create(raw=raw)

    @staticmethod
    def retrieve(self):
        """
        It should implemented by child
        :return:
        """
        pass  # pragma: no cover
