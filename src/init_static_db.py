from src.dao.AreaManager import AreaManager
from src.dao.BuildingManager import BuildingManager
from src.dao.SnifferManager import SnifferManager

from src.models.area import Area
from src.models.building import Building
from src.models.sniffer import Sniffer

import json


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
    building.name = "Polo Fibonacci"
    building.id_user = 1
    building.id_zerynth = "abcd1234"
    BuildingManager.add(building)


def init_sniffers():
    sn1 = Sniffer()
    sn1.id_zerynth = "abcd1234"
    sn1.id_building = 1
    sn1.name = "Sniffer 1"
    sn1.x = 0
    sn1.y = 7.8

    sn2 = Sniffer()
    sn2.id_zerynth = "efgh5678"
    sn2.id_building = 1
    sn2.name = "Sniffer 2"
    sn2.x = 5.1
    sn2.y = 1.5

    sn3 = Sniffer()
    sn3.id_zerynth = "ijkl9012"
    sn3.id_building = 1
    sn3.name = "Sniffer 3"
    sn3.x = 9.3
    sn3.y = 7.8

    SnifferManager.add(sn1)
    SnifferManager.add(sn2)
    SnifferManager.add(sn3)
