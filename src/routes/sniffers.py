from src import app

from src.dao.SnifferManager import SnifferManager
from src.models.Sniffer import Sniffer


@app.route("/sniffers/push/")
def push_sniffer():
    sniffer = Sniffer()
    sniffer.name = "TEST Sniffer"
    sniffer.id_building = 1
    sniffer.id_zerynth = "abcd1234"
    sniffer.x = 0
    sniffer.y = 0
    SnifferManager.add(sniffer)
    return "<p>Sniffer pushed</p>"


@app.route("/sniffers/pull/")
def pull_sniffers():
    sniffers = SnifferManager.get_all()
    return sniffers
