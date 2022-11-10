from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.test import blueprints

import datetime

db = SQLAlchemy()

def create_app():

    global db

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db = SQLAlchemy(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    for bp in blueprints:
        app.register_blueprint(bp)
        bp.app = app
        
    # db_disk = sl.connect('database.db')
    # db_mem = sl.connect(':memory:')
    # db_disk.backup(db_mem)
    print("DEBUG: Database loaded")
    # db_mem.backup(db_disk) # write db to disk
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=10001)
