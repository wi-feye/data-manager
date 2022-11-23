from src import app

from src.dao.AreaManager import AreaManager
from src.models.area import Area


@app.route("/api/areas/push/")
def push_area():
    area = Area()
    area.name = "TEST Area"
    area.id_building = 1
    area.location = "[[0,0],[0,0],[0,0],[0,0]]"
    AreaManager.add(area)
    return {"status": True, "message": "Area pushed"}


@app.route("/api/areas/pull/")
def pull_areas():
    areas = AreaManager.get_all()
    return areas


@app.route("/api/areas/pull/<id_building>/")
def pull_areas_by_building(id_building):
    areas = AreaManager.get_areas_by_building(id_building)
    return areas
