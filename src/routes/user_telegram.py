import json
from random import randint
from src import app
from flask import request

from src.dao.UserTelegramManager import UserTelegramManager

@app.route("/api/user_telegram/gen_tmpcode/<id_user>", methods=["POST"])
def gen_tmpcode(id_user):
    tmpcode = randint(100000, 999999)
    UserTelegramManager.gen_tmpcode(id_user, tmpcode)
    return {"status": True, "tmpcode": tmpcode}

@app.route("/api/user_telegram/add_chatid/", methods=["POST"])
def add_chatid():
    body = json.loads(request.data)
    tmpcode = body["tmpcode"]
    chatid = body["chatid"]
    user_telegram = UserTelegramManager.add_chatid(tmpcode, chatid)
    return {"status": user_telegram is not None, "user_telegram": user_telegram}

@app.route("/api/user_telegram/enabled_toggle/<id_user>", methods=["POST"])
def enabled_toggle(id_user):
    UserTelegramManager.enabled_toggle(id_user)
    return {"status": True}

@app.route("/api/user_telegram/get/<id_user>", methods=["GET"])
def get(id_user):
    return UserTelegramManager.get(id_user)

@app.route("/api/user_telegram/delete/<id_user>", methods=["DELETE"])
def delete(id_user):
    UserTelegramManager.delete(id_user)
    return {"status": True}


