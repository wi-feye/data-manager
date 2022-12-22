from src import db
from src.dao.manager import Manager
from src.models.user_telegram import UserTelegram
from datetime import datetime, timedelta

from src import db 

class UserTelegramManager(Manager):
    @staticmethod
    def gen_tmpcode(id_user: int, tmpcode: int):
        UserTelegram.query.filter_by(id_user=id_user).delete()
        db.session.commit()
        user_telegram = UserTelegram()
        user_telegram.id_user = id_user
        user_telegram.tmpcode = tmpcode
        user_telegram.enabled = True
        user_telegram.gencode_timestamp = datetime.now().isoformat()
        Manager.create(user_telegram=user_telegram)

    @staticmethod
    def add_chatid(tmpcode, chatid):
        user_telegram = UserTelegram.query.filter_by(tmpcode=tmpcode).first()
        if user_telegram is not None:
            threshold = datetime.now() - timedelta(minutes=10)
            if user_telegram.gencode_timestamp is not None and user_telegram.gencode_timestamp > threshold:
                UserTelegram.query.filter_by(id_user=user_telegram.id_user).update({
                    "chatid": chatid, 
                    "gencode_timestamp": None,
                    "tmpcode": None,
                })
                db.session.commit()
                return user_telegram_dict(user_telegram)
        return None

    @staticmethod
    def get(id_user: int):
        user_telegram = UserTelegram.query.filter_by(id_user=id_user).first()
        if user_telegram is not None:
            return user_telegram_dict(user_telegram)
        else:
            return {}

    @staticmethod
    def delete(id_user: int):
        UserTelegram.query.filter_by(id_user=id_user).delete()
        db.session.commit()

    @staticmethod
    def enabled_toggle(id_user: int):
        user_telegram = UserTelegram.query.filter_by(id_user=id_user).first()
        if user_telegram is not None:
            UserTelegram.query.filter_by(id_user=id_user).update({
                "enabled": not user_telegram.enabled
            })
            db.session.commit()
      

def user_telegram_dict(user_telegram):
    return {
        "id_user": user_telegram.id_user,
        "chatid": user_telegram.chatid,
        "tmpcode": user_telegram.tmpcode,
        "enabled": user_telegram.enabled,
        "gencode_timestamp": None if user_telegram.gencode_timestamp is None else user_telegram.gencode_timestamp.isoformat(),
    }
