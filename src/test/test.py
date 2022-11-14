from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import url_for

from datetime import datetime, date
from src.models.Raw import Raw
from src.dao.RawManager import RawManager

# from flask_mail import Mail, Message

test = Blueprint("test", __name__)

@test.route("/")
def hello_world():
    print('Hello world')    
    return "<p>Hello, World!</p>"

@test.route("/api/")
def api():
    return "<p>API Handle</p>"

@test.route("/push/")
def push():
    raw = Raw(datetime.now, 'macaddress', 1, 2, 3)
    RawManager.create(raw)