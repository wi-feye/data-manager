from src import app

from flask import request
from src.dao.Device_DetectionManager import DeviceManager
from src.models.position_detection import Device_Detection
import json


@app.route("/api/ai/create-position-detections/", methods=["POST"])
def push_data():
    received_data = json.loads(request.data)

    for position in received_data:
        dd = Device_Detection()
        dd.x = position["x"]
        dd.y = position["y"]
        dd.id_area = position["id_area"]
        dd.id_building = position["id_building"]
        dd.timestamp = position["timestamp"]
        DeviceManager.add(dd)

    return "<p>Records pushed</p>"


# /api/position-detection/pull/<id_building>?start=start&end=end/
@app.route("/api/position-detection/pull/<id_building>")
def pull_data(id_building):
    start_time = request.args.get("start")
    end_time = request.args.get("end")
    print(id_building, start_time, end_time)

    data = DeviceManager.get_data_by_timestamp_by_building(
        id_building, start_time, end_time
    )
    return json.dumps(data)

