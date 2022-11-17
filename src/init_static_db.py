from src.dao.AreaManager import AreaManager
from src.models.area import Area

import json

def init_areas():
    x2 = Area()
    x2.name = 'X2'
    x2.id_building = 1
    x2.location = json.dumps([[5,-0.5],[9.8,-0.5],[9.8,8.3],[5,8.3]])

    x3 = Area()
    x3.name = 'X3'
    x3.id_building = 1
    x3.location = json.dumps([[-1,-0.5],[5,-0.5],[5,8.3],[-1,8.3]])

    corridoio = Area()
    corridoio.name = 'Corridoio'
    corridoio.id_building = 1
    corridoio.location = json.dumps([[-1,-3],[9.8,-3],[9.8,-0.5],[-1,-0.5]])

    AreaManager.add(x2)
    AreaManager.add(x3)
    AreaManager.add(corridoio)