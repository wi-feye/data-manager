from src.dao.Device_DetectionManager import DeviceManager
from src.dao.AreaManager import AreaManager
from src.dao.BuildingManager import BuildingManager
from src.dao.RawManager import RawManager
from src.dao.SnifferManager import SnifferManager

from src.models.area import Area
from src.models.building import Building
from src.models.sniffer import Sniffer
from src.models.raw import Raw
from src.models.position_detection import Device_Detection

import json
from datetime import datetime


def init_areas():
    with open("init_files/areas.json") as f:
        areas = json.load(f)
        for area in areas:
            a = Area()
            a.id_building = area["id_building"]
            a.name = area["name"]
            a.description = area["description"]
            a.location = area["location"]
            AreaManager.add(a)


def init_buildings():
    with open("init_files/buildings.json") as f:
        buildings = json.load(f)
        for building in buildings:
            b = Building()
            b.name = building["name"]
            b.id_user = building["id_user"]
            b.id_zerynth = building["id_zerynth"]
            b.lastupdate = building["lastupdate"]
            BuildingManager.add(b)


def init_sniffers():
    with open("init_files/sniffers.json") as f:
        sniffers = json.load(f)
        for sniffer in sniffers:
            s = Sniffer()
            s.id_building = sniffer["id_building"]
            s.id_zerynth = sniffer["id_zerynth"]
            s.name = sniffer["name"]
            s.x = sniffer["x"]
            s.y = sniffer["y"]
            SnifferManager.add(s)


def init_raw_data():
    with open("init_files/raw_data.json") as f:
        raw_data = json.load(f)
        for building in raw_data:
            id_building = building["id_building"]
            records = building["records"]
            lastupdate = building["lastupdate"]
            BuildingManager.update_by_id(id_building, {"lastupdate": lastupdate})
            for record in records:
                raw = Raw()
                raw.id_building = id_building
                raw.timestamp = record["timestamp"]
                raw.mac_hash = record["mac_hash"]
                rssi_list = []
                for rssi in record["rssi_device"]:
                    rssi_list.append([rssi["id"], rssi["rssi"]])
                raw.rssi_device = rssi_list
                RawManager.add(raw)


def init_positions():
    with open("init_files/positions.json") as f:
        positions = json.load(f)
        for position in positions:
            dd = Device_Detection()
            dd.x = position["x"]
            dd.y = position["y"]
            dd.id_area = position["id_area"]
            dd.id_building = position["id_building"]
            dd.timestamp = position["timestamp"]
            DeviceManager.add(dd)
            RawManager.delete_by_id(position["id"])
