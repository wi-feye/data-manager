from src.models.raw import Raw
from src.dao.RawManager import RawManager
from src import app
from datetime import datetime


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/")
def api():
    return "<p>API Handle</p>"

@app.route("/push/")
def push():
    raw = Raw()
    raw.timestamp = datetime.now()
    raw.mac = 'macaddress'
    raw.rssi_1 = 1
    raw.rssi_2 = 2
    raw.rssi_3 = 3
    RawManager.add(raw)
    return "<p>Data pushed</p>"

@app.route("/pull/")
def pull():
    raws = RawManager.get_all()
    return raws