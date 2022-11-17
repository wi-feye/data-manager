from src import app

from src.dao.BuildingManager import BuildingManager
from src.models.Building import Building

@app.route("/buildings/push/")
def push_building():
    building = Building()
    building.name = 'TEST Building'
    building.id_user = 1
    building.id_zerynth = 'efgh5678'
    BuildingManager.add(building)
    return "<p>Building pushed</p>"

@app.route("/buildings/pull/")
def pull_buildings():
    buildings = BuildingManager.get_all()
    return buildings