from src import app

from src.dao.BuildingManager import BuildingManager
from src.dao.AreaManager import AreaManager
from src.dao.SnifferManager import SnifferManager

from src.models.building import Building
from src.models.area import Area
from src.models.sniffer import Sniffer

from datetime import datetime

import json


# @app.route("/api/buildings/push/")
# def push_building():
#     building = Building()
#     building.name = "TEST Building"
#     building.id_user = 1
#     building.id_zerynth = "efgh5678"
#     building.lastupdate = datetime.now().isoformat()
#     BuildingManager.add(building)
#     return {"status": True, "message": "Building pushed"}


@app.route("/api/buildings/pull/")
def pull_buildings():
    buildings = BuildingManager.get_all()
    return buildings


@app.route("/api/buildings/pull/<id_user>/")
def pull_buildings_by_user(id_user):
    buildings = BuildingManager.get_buildings_by_user(id_user)
    return buildings

    