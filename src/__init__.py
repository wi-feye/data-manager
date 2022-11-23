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

    db = SQLAlchemy(app=app)

    from src.models.raw import Raw
    from src.models.building import Building
    from src.models.area import Area
    from src.models.position_detection import Device_Detection
    from src.models.sniffer import Sniffer

    migrate = Migrate(app=app, db=db)

    from src.routes import general
    from src.routes import raw_data
    from src.routes import areas
    from src.routes import buildings
    from src.routes import sniffers
    from src.routes import detection_device

    app.app_context().push()
    db.create_all()

    # Static db initialization
    from src import init_static_db

    if areas.pull_areas() == []:
        print("Initializing areas in db")
        init_static_db.init_areas()
    if buildings.pull_buildings() == []:
        print("Initializing buildings in db")
        init_static_db.init_buildings()
    if sniffers.pull_sniffers() == []:
        print("Initializing sniffers in db")
        init_static_db.init_sniffers()
    if raw_data.pull_raw() == []:
        print("Initializing raw data in db")
        init_static_db.init_raw_data()
    if detection_device.pull_data() == []:
        print("Initializing positions in db")
        init_static_db.init_positions()

    return app
