from src import app

from src.dao.RawManager import RawManager
from src.models.Raw import Raw

from datetime import datetime


@app.route("/raw/push/")
def push_raw():
    raw = Raw()
    raw.timestamp = datetime.now()
    raw.mac = "macaddress"
    raw.rssi_1 = 1
    raw.rssi_2 = 2
    raw.rssi_3 = 3
    RawManager.add(raw)
    return "<p>Data pushed</p>"


@app.route("/raw/pull/")
def pull_raw():
    raws = RawManager.get_all()
    return raws
