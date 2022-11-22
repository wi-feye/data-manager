from src import app

from flask import request
import json

from src.dao.BuildingManager import BuildingManager
from src.dao.AreaManager import AreaManager
from src.dao.SnifferManager import SnifferManager
from src.dao.RawManager import RawManager

from src.models.building import Building
from src.models.area import Area
from src.models.sniffer import Sniffer
from src.models.raw import Raw


@app.route("/api/")
def hello():
    return "<p>API Handle</p>"


@app.route("/api/query")  # /api/query?name=Test
def test_query():
    name = request.args.get("name")
    return f"<p>name={name}</p>"


@app.route("/api/details/datacollector/")
def details_datacollector():
    details_dict = []
    buildings = BuildingManager.get_all()
    
    for building in buildings:
        id_building = building["id"]
        single_building = {
            "id": id_building,
            "id_user": building["id_user"],
            "id_zerynth": building["id_zerynth"],
            "lastupdate": building["lastupdate"],
        }
       
        sniffers = SnifferManager.get_sniffers_by_building(id_building)

        single_building["sniffers"] = sniffers
        details_dict.append(single_building)

    return json.dumps(details_dict)

@app.route("/api/details/ai/")
def details_ai():
    details_dict = []
    buildings = BuildingManager.get_all()
    
    for building in buildings:
        id_building = building["id"]
        single_building = {}
        single_building["id"] = id_building

        raws = RawManager.get_raw_data_by_building_start_time(
            id_building, building["lastupdate"] # occhio a lastupdate
        )
        if len(raws) == 0:
            continue

        sniffers = SnifferManager.get_sniffers_by_building(id_building)
        areas = AreaManager.get_areas_by_building(id_building)
        single_building["areas"] = areas
        single_building["sniffers"] = sniffers
        single_building["raws"] = raws
        details_dict.append(single_building)

    return json.dumps(details_dict)
