from src.models.raw import Raw
from src.models.area import Area
from src.models.building import Building

from src.dao.RawManager import RawManager
from src.dao.AreaManager import AreaManager
from src.dao.BuildingManager import BuildingManager

from src import app
from datetime import datetime


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/")
def api():
    return "<p>API Handle</p>"

@app.route("/push/raw")
def push_raw():
    raw = Raw()
    raw.timestamp = datetime.now()
    raw.mac = 'macaddress'
    raw.rssi_1 = 1
    raw.rssi_2 = 2
    raw.rssi_3 = 3
    RawManager.add(raw)
    return "<p>Data pushed</p>"

@app.route("/pull/raw/")
def pull_raw():
    raws = RawManager.get_all()
    return raws

@app.route("/pull/areas/")
def pull_areas():
    areas = AreaManager.get_all()
    return areas