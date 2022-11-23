from src import app

from src.dao.RawManager import RawManager
from src.dao.BuildingManager import BuildingManager
from src.models.raw import Raw

from datetime import datetime
from flask import request
import json


# @app.route("/api/raw/push/")
# def push_raw():
#     raw = Raw()
#     raw.id_building = 1
#     raw.timestamp = datetime.now().isoformat()
#     raw.mac_hash = "test_macaddr1234"
#     raw.rssi_device = [[1234, -50], [5678, -10], [9012, -20]]
#     RawManager.add(raw)
#     return {"status": True, "message": "Data pushed"}


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
        id_building = building["id_building"]
        records = building["records"]
        lastupdate =  building["lastupdate"]
        BuildingManager.update_by_id(id_building, {"lastupdate": lastupdate})
        for record in records:
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
