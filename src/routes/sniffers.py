from src import app

from src.dao.SnifferManager import SnifferManager
from src.models.sniffer import Sniffer


# @app.route("/api/sniffers/push/")
# def push_sniffer():
#     sniffer = Sniffer()
#     sniffer.name = "TEST Sniffer"
#     sniffer.id_building = 1
#     sniffer.id_zerynth = "abcd1234"
#     sniffer.x = 0
#     sniffer.y = 0
#     SnifferManager.add(sniffer)
#     return {"status": True, "message": "Sniffer pushed"}


@app.route("/api/sniffers/pull/")
def pull_sniffers():
    sniffers = SnifferManager.get_all()
    return sniffers


@app.route("/api/sniffers/pull/<id_building>/")
def pull_sniffers_by_building(id_building):
    sniffers = SnifferManager.get_sniffers_by_building(id_building)
    return sniffers
