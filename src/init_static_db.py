from src.dao.Device_DetectionManager import DeviceManager
from src.dao.AreaManager import AreaManager
from src.dao.BuildingManager import BuildingManager
from src.dao.RawManager import RawManager
from src.dao.SnifferManager import SnifferManager

from src.models.area import Area
from src.models.building import Building
from src.models.sniffer import Sniffer

import json
from datetime import datetime


def init_areas():
    x2 = Area()
    x2.name = "X2"
    x2.id_building = 1
    x2.location = json.dumps([[5, -0.5], [9.8, -0.5], [9.8, 8.3], [5, 8.3]])

    x3 = Area()
    x3.name = "X3"
    x3.id_building = 1
    x3.location = json.dumps([[-1, -0.5], [5, -0.5], [5, 8.3], [-1, 8.3]])

    corridoio = Area()
    corridoio.name = "Corridoio"
    corridoio.id_building = 1
    corridoio.location = json.dumps([[-1, -3], [9.8, -3], [9.8, -0.5], [-1, -0.5]])

    AreaManager.add(x2)
    AreaManager.add(x3)
    AreaManager.add(corridoio)


def init_buildings():
    building = Building()
    building.name = "Smart Application project"
    building.id_user = 1
    building.id_zerynth = "wks-7e2yv6y5ijmc"
    building.lastupdate = "2020-11-22T00:00:00"
    BuildingManager.add(building)


def init_sniffers():
    sn1 = Sniffer()
    sn1.id_zerynth = "dev-7e30tm36tedz"
    sn1.id_building = 1
    sn1.name = "Sniffer 1"
    sn1.x = 0
    sn1.y = 7.8

    sn2 = Sniffer()
    sn2.id_zerynth = "dev-7e31vzpgzg2h"
    sn2.id_building = 1
    sn2.name = "Sniffer 2"
    sn2.x = 5.1
    sn2.y = 1.5

    sn3 = Sniffer()
    sn3.id_zerynth = "dev-7e328j1uzw9m"
    sn3.id_building = 1
    sn3.name = "Sniffer 3"
    sn3.x = 9.3
    sn3.y = 7.8

    SnifferManager.add(sn1)
    SnifferManager.add(sn2)
    SnifferManager.add(sn3)