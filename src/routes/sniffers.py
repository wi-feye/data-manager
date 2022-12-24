from src import app

from src.dao.SnifferManager import SnifferManager
from src.models.sniffer import Sniffer
from flask import request

import json


@app.route("/api/sniffers/push/", methods=["POST"])
def push_sniffer():
    received_sniffer = json.loads(request.data)

    sniffer = Sniffer()
    sniffer.name = received_sniffer["name"]
    sniffer.id_building = received_sniffer["id_building"]
    sniffer.id_zerynth = received_sniffer["id_zerynth"]
    sniffer.x = received_sniffer["x"]
    sniffer.y = received_sniffer["y"]
    SnifferManager.add(sniffer)
    return {"status": True, "message": "Sniffer pushed"}


@app.route("/api/sniffers/delete/<id_sniffer>/", methods=["DELETE"])
def delete_sniffer_by_user(id_sniffer):
    SnifferManager.delete_sniffer_by_id(id_sniffer)
    return {"status": True, "message": "sniffer deleted"}


@app.route("/api/sniffers/update/<id_sniffer>/", methods=["POST"])
def update_sniffer(id_sniffer):
    received_sniffer = json.loads(request.data)
    SnifferManager.update_by_id(id_sniffer, received_sniffer)
    return {"status": True, "message": "sniffer updated"}


@app.route("/api/sniffers/pull/")
def pull_sniffers():
    sniffers = SnifferManager.get_all()
    return sniffers


@app.route("/api/sniffers/pull/<id_building>/")
def pull_sniffers_by_building(id_building):
    sniffers = SnifferManager.get_sniffers_by_building(id_building)
    return sniffers
