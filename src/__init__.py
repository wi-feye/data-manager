from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from datetime import datetime

import redis

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,db)

with app.app_context():
    if db.engine.url.drivername == 'sqlite':
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

redis_client = redis.StrictRedis( 
                host='127.0.0.1',
                port=5342,
                db='/data_manager.db')

from src.models.Raw import Raw
from src.dao.RawManager import RawManager

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

#app = None
#db = SQLAlchemy()
#migrate = Migrate()


#def create_app():
#global db

    # app = Flask(__name__)
    # app.config.from_object(Config)

    # #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

    # db.init_app(app=app)
    # migrate.init_app(app=app, db=db)

    # with app.app_context():
    #     if db.engine.url.drivername == 'sqlite':
    #         migrate.init_app(app, db, render_as_batch=True)
    #     else:
    #         migrate.init_app(app, db)

    # for bp in blueprints:
    #     app.register_blueprint(bp)
    #     bp.app = app
        
    # # db_disk = sl.connect('database.db')
    # # db_mem = sl.connect(':memory:')
    # # db_disk.backup(db_mem)
    # print("DEBUG: Database loaded")
    # # db_mem.backup(db_disk) # write db to disk


# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=10001)

# class ProdConfig(DevConfig):
#     """
#     This is the main configuration object for application.
#     """
#     TESTING = False
#     DEBUG = False

#     import os
#     SECRET_KEY = os.getenv('APP_SECRET', os.urandom(24))

#     SQLALCHEMY_ECHO = False
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     POSTGRES_USER = os.getenv('POSTGRES_USER', None)
#     POSTGRES_PASS = os.getenv('POSTGRES_PASSWORD', None)
#     POSTGRES_DB = os.getenv('POSTGRES_DB', None)
#     POSTGRES_HOST = os.getenv('POSTGRES_HOST', None)
#     POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
#     SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
#         POSTGRES_USER, POSTGRES_PASS, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB)