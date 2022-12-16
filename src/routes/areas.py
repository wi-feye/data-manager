import json
from src import app

from src.dao.Device_DetectionManager import DeviceManager
from src.dao.AreaManager import AreaManager
from src.models.area import Area

from flask import request



@app.route("/api/areas/push/", methods=["POST"])
def push_area():
    received_area = json.loads(request.data)
    area = Area()
    area.name = received_area["name"]
    area.id_building = received_area["id_building"]
    area.location = str(received_area["location"])
    if "color" in received_area:
        area.color = received_area["color"]
    if "description" in received_area:
        area.description = received_area["description"]
    AreaManager.add(area)
    return {"status": True, "message": "Area pushed"}

@app.route("/api/areas/delate/<id_area>/", methods=["DELETE"])
def delete_area_by_area(id_area):
    AreaManager.delete_area_by_id(id_area)
    return {"status": True, "message": "Area pushed"}

@app.route("/api/areas/update/<id_area>/", methods=["POST"])
def update_area(id_area):   
    received_area = json.loads(request.data)   
    AreaManager.update_area_id(id_area, received_area)
    return {"status": True, "message": "Area updated"}
  

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
