from src import app

from src.dao.BuildingManager import BuildingManager
from src.models.building import Building

from datetime import datetime


@app.route("/api/buildings/push/")
def push_building():
    building = Building()
    building.name = "TEST Building"
    building.id_user = 1
    building.id_zerynth = "efgh5678"
    building.lastupdate = datetime.now()
    BuildingManager.add(building)
    return "<p>Building pushed</p>"


@app.route("/api/buildings/pull/")
def pull_buildings():
    buildings = BuildingManager.get_all()
    return buildings


@app.route("/api/buildings/pull/<id_user>/")
def pull_buildings_by_user(id_user):
    buildings = BuildingManager.get_buildings_by_user(id_user)
    return buildings
