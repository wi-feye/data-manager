from src.dao.manager import Manager
from src.models.User import User

class UserManager(Manager):

    @staticmethod
    def create_user(user: User):
        Manager.create(user=user)
