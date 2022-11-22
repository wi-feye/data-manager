from src import app

from src.dao.RawManager import RawManager
from src.models.raw import Raw

from datetime import datetime


@app.route("/api/raw/push/")
def push_raw():
    raw = Raw()
    raw.id_building = 1
    raw.timestamp = datetime.now()
    raw.mac_hash = "test_macaddr1234"
    raw.rssi_device = [[1234, -50], [5678, -10], [9012, -20]]
    RawManager.add(raw)
    return "<p>Data pushed</p>"


@app.route("/api/raw/pull/")
def pull_raw():
    raws = RawManager.get_all()
    return raws


@app.route("/api/raw/pull/<id_building>/<start_time>/<end_time>/")
def pull_raw_by_time_interval(id_building, start_time, end_time):
    n_raw_data = RawManager.get_raw_data_by_time_interval_by_building(
        id_building, start_time, end_time
    )
    return str(len(n_raw_data))
