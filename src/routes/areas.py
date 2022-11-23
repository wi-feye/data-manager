import json
from src import app

from src.dao.Device_DetectionManager import DeviceManager
from src.dao.AreaManager import AreaManager
from src.models.area import Area

from flask import request


# @app.route("/api/areas/push/")
# def push_area():
#     area = Area()
#     area.name = "TEST Area"
#     area.id_building = 1
#     area.location = "[[0,0],[0,0],[0,0],[0,0]]"
#     AreaManager.add(area)
#     return {"status": True, "message": "Area pushed"}


@app.route("/api/areas/pull/")
def pull_areas():
    areas = AreaManager.get_all()
    return areas


@app.route("/api/areas/pull/<id_building>/")
def pull_areas_by_building(id_building):
    areas = AreaManager.get_areas_by_building(id_building)
    return areas


@app.route("/api/areas_with_position_detections/pull/<id_building>/")
def areas_with_position_detections_by_building(id_building):

    start_time = request.args.get("start")
    end_time = request.args.get("end")

    areas = AreaManager.get_areas_by_building(id_building)

    for area in areas:
        area["position_detections"] = DeviceManager.get_data(id_building=id_building, id_area=area["id"], start_time=start_time, end_time=end_time)

    return json.dumps(areas)
