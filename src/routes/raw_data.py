from src import app

from src.dao.RawManager import RawManager
from src.dao.BuildingManager import BuildingManager
from src.dao.SnifferManager import SnifferManager
from src.models.raw import Raw

from datetime import datetime
from flask import request
import json
import requests

apiToken = ""
chat_id = ""

with open("init_files/telegram.json", "r") as f:
    data = json.load(f)
    apiToken = data["apiToken"]
    chat_id = data["chat_id"]


def send_telegram_msg(message):
    url = f"https://api.telegram.org/bot{apiToken}/sendMessage"
    try:
        requests.post(url, json={"chat_id": chat_id, "text": message})
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
    global last_notification
    received_data = json.loads(request.data)

    for building in received_data:
        building_db = BuildingManager.get_building_by_id(building["id_building"])

        id_building = building["id_building"]
        records = building["records"]
        lastupdate = building["lastupdate"]

        # Send telegram message for offline sniffers in the building
        sniffers = SnifferManager.get_sniffers_by_building(id_building)
        for sniffer in sniffers:
            now = datetime.now()
            response = requests.get(
                "https://api.zdm.zerynth.com/v3/workspaces/" + building_db["id_zerynth"] + "/devices/" + sniffer["id_zerynth"], 
                headers={"X-API-KEY": "G9froN8D4R.cF1znVzGvCejjc5BrzCsSqcqMaANPgRmFXMglCAWhkYttQFTymThnrf1ta7OQVP4"}
            ).json()
            online = (response["device"])["is_connected"]
            if not online:
                last_sniffer_notification = SnifferManager.get_sniffer_by_id(sniffer["id"])["last_tg_notification"]
                gap = now - last_sniffer_notification
                if (gap.seconds / 60) > 30:
                    if send_telegram_msg("Sniffer " + sniffer["name"] + " in building " + building_db["name"] + " is offline"):
                        last_sniffer_notification = now
                        SnifferManager.update_by_id(sniffer["id"], {"last_tg_notification": last_sniffer_notification})

        # Send telegram message for anomalies in closed buildings
        BuildingManager.update_by_id(id_building, {"lastupdate": lastupdate})
        for record in records:
            now = datetime.now()
            time = datetime.fromisoformat(record["timestamp"][:-1])
            last_building_notification = building_db["last_tg_notification"]
            gap = now - last_building_notification
            if (gap.seconds / 60) > 30:
                if not BuildingManager.is_open_by_time(id_building, time):
                    if send_telegram_msg("Activity detected in building " + building_db["name"]):
                        last_building_notification = now
                        BuildingManager.update_by_id(id_building, {"last_tg_notification": last_building_notification})

            raw = Raw()
            raw.id_building = id_building
            raw.timestamp = record["timestamp"]
            raw.mac_hash = record["mac_hash"]
            rssi_list = []
            for rssi in record["rssi_device"]:
                rssi_list.append([rssi["id"], rssi["rssi"]])
            raw.rssi_device = rssi_list
            RawManager.add(raw)

    return {"status": True, "message": "Records pushed"}
