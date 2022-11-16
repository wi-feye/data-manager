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

    from src import routes

    app.app_context().push()
    db.create_all()

    import src.init_static_db as init_db

    init_db.init_areas()

    return app
    