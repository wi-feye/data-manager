from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = None
db = None
migrate = None

def create_app():
    global app
    global db
    global migrate

    app = Flask(__name__)
    app.config.from_object(Config)

    # env = Environments(app)
    # env.from_object(Config)

    db = SQLAlchemy(
        app=app
    )

    from src.models.raw import Raw
    from src.models.building import Building
    from src.models.area import Area
    from src.models.device_detection import Device_Detection
    from src.models.crowd import Crowd
    from src.models.sniffer import Sniffer

    migrate = Migrate(
        app=app,
        db=db
    )

    from src.routes import test
    from src.routes import raw_data
    from src.routes import areas
    # from src.routes import building_data
    # from src.routes import device_detection_data
    # from src.routes import crowd_data
    # from src.routes import sniffer_data

    app.app_context().push()
    db.create_all()

    from src import init_static_db

    from src.dao.AreaManager import AreaManager
    if AreaManager.get_all() == []: #TODO: sostituire con la rispettiva funzione delle routes per le aree cosi da non chiamare il dao/manager da qui
        init_static_db.init_areas()

    return app
    