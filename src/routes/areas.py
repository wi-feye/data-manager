from src import app

from src.dao.AreaManager import AreaManager
from src.models.Area import Area


@app.route("/areas/push/")
def push_area():
    area = Area()
    area.name = "TEST Area"
    area.id_building = 1
    area.location = "[[0,0],[0,0],[0,0],[0,0]]"
    AreaManager.add(area)
    return "<p>Area pushed</p>"


@app.route("/areas/pull/")
def pull_areas():
    areas = AreaManager.get_all()
    return areas
