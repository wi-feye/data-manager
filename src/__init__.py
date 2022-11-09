from flask import Flask
import sqlite3 as sl

def create_app():
    app = Flask(__name__)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    # )
    app.config['APPLICATION_ROOT'] = '/api/'
    # Load db
    db_disk = sl.connect('database.db')
    db_mem = sl.connect(':memory:')
    db_disk.backup(db_mem)
    print("DEBUG: Database loaded")
    # db_mem.backup(db_disk) # write db to disk
    return app

app = create_app()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/")
def api():
    return "<p>API Handle</p>"