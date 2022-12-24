from src import app

from src.dao.BuildingManager import BuildingManager
from src.dao.AreaManager import AreaManager
from src.dao.SnifferManager import SnifferManager

from src.models.building import Building
from src.models.area import Area
from src.models.sniffer import Sniffer

from datetime import datetime

from flask import request

import json


@app.route("/api/buildings/push/", methods=["POST"])
def push_building():

    received_building = json.loads(request.data)
    building = Building()
    building.name = received_building["name"]
    building.id_user = received_building["id_user"]
    building.id_zerynth = received_building["id_zerynth"]
    building.open_time = received_building["open_time"]
    building.close_time = received_building["close_time"]
    building.lastupdate = datetime.now().isoformat()
    BuildingManager.add(building)
    return {"status": True, "message": "Building pushed"}


@app.route("/api/buildings/pull/")
def pull_buildings():
    buildings = BuildingManager.get_all()
    return buildings


@app.route("/api/buildings/pull/<id_user>/")
def pull_buildings_by_user(id_user):
    buildings = BuildingManager.get_buildings_by_user(id_user)
    return buildings


@app.route("/api/buildings/delete/<id_building>/", methods=["DELETE"])
def delete_buildings_by_user(id_building):
    BuildingManager.delete_building_by_id(id_building)
    return {"status": True, "message": "Building deleted"}


@app.route("/api/buildings/update/<id_building>/", methods=["POST"])
def update_building(id_building):
    received_building = json.loads(request.data)
    BuildingManager.update_by_id(id_building, received_building)
    return {"status": True, "message": "Building updated"}
