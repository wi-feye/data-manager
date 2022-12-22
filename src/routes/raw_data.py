from src import app

from src.dao.RawManager import RawManager
from src.dao.BuildingManager import BuildingManager
from src.dao.SnifferManager import SnifferManager
from src.dao.UserTelegramManager import UserTelegramManager
from src.models.raw import Raw

from datetime import datetime
from flask import request
import json
import requests
from dotenv import dotenv_values

config = dotenv_values('env_file')
TELEGRAM_TOKEN = config["TELEGRAM_TOKEN"]
USER_MANAGER_HOST = config["USER_MANAGER_HOST"]
THRESHOLD_GAP = int(config["THRESHOLD_GAP"]) if "THRESHOLD_GAP" in config else 30


def send_telegram_msg(chatid, message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": chatid, "text": message})
        return True
    except Exception as e:
        print("Error occurred sending Telegram message:", e)
        return False


@app.route("/api/raw/pull/")
def pull_raw():
    raws = RawManager.get_all()
    return raws


# /api/raw/pull/<id_building>?start=start&end=end/
@app.route("/api/raw/pull/<id_building>")
def pull_raw_by_time_interval(id_building):
    start_time = request.args.get("start")
    end_time = request.args.get("end")
    n_raw_data = RawManager.get_raw_data_by_time_interval_by_building(
        id_building, start_time, end_time
    )
    return str(len(n_raw_data))


@app.route("/api/raw/push/datacollector/", methods=["POST"])
def push_raw_datacollector():
    received_data = json.loads(request.data)

    for building in received_data:
        building_db = BuildingManager.get_building_by_id(building["id_building"])

        id_user = building_db["id_user"]
        user = requests.get(f"{USER_MANAGER_HOST}/user?id={id_user}").json()
        api_key = user["apikey_zerynth"]

        user_telegram = UserTelegramManager.get(id_user)
        chatid = None
        if "chatid" in user_telegram and user_telegram["enabled"]:
            chatid = user_telegram["chatid"]

        last_building_notification = datetime.fromisoformat(building_db["last_tg_notification"])

        id_building = building["id_building"]
        records = building["records"]
        lastupdate = building["lastupdate"]

        # Send telegram message for offline sniffers in the building
        if chatid is not None:
            sniffers = SnifferManager.get_sniffers_by_building(id_building)
            for sniffer in sniffers:
                now = datetime.now()
                response = requests.get(
                    "https://api.zdm.zerynth.com/v3/workspaces/" + building_db["id_zerynth"] + "/devices/" + sniffer["id_zerynth"], 
                    headers={"X-API-KEY": api_key}
                ).json()
                online = (response["device"])["is_connected"]
                if not online:
                    last_sniffer_notification = SnifferManager.get_sniffer_by_id(sniffer["id"])["last_tg_notification"]
                    gap = now - datetime.fromisoformat(last_sniffer_notification)
                    if (gap.seconds / 60) > THRESHOLD_GAP:
                        if send_telegram_msg(chatid, "Sniffer " + sniffer["name"] + " in building " + building_db["name"] + " is offline"):
                            last_sniffer_notification = now
                            SnifferManager.update_by_id(sniffer["id"], {"last_tg_notification": last_sniffer_notification})

        # Send telegram message for anomalies in closed buildings
        BuildingManager.update_by_id(id_building, {"lastupdate": lastupdate})
        for record in records:

            if chatid is not None:
                now = datetime.now()
                time = datetime.fromisoformat(record["timestamp"][:-1])
                gap = now - last_building_notification
                if (gap.seconds / 60) > THRESHOLD_GAP:
                    if not BuildingManager.is_open_by_time(id_building, time):
                        if send_telegram_msg(chatid, "Activity detected in building " + building_db["name"]):
                            last_building_notification = now

            raw = Raw()
            raw.id_building = id_building
            raw.timestamp = record["timestamp"]
            raw.mac_hash = record["mac_hash"]
            rssi_list = []
            for rssi in record["rssi_device"]:
                rssi_list.append([rssi["id"], rssi["rssi"]])
            raw.rssi_device = rssi_list
            RawManager.add(raw)

        BuildingManager.update_by_id(id_building, {"last_tg_notification": last_building_notification})

    return {"status": True, "message": "Records pushed"}
