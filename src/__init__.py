from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import sqlite3 as sl
import os
#DB = '

def create_app():
    app = Flask(__name__)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    # ) 
    # app.config['APPLICATION_ROOT'] = '/api/'
    # # Load db
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    # db = SQLAlchemy(app)
    # db.create_all()

    # db_disk = sl.connect('database.db')
    # db_mem = sl.connect(':memory:')
    # db_disk.backup(db_mem)
    print("DEBUG: Database loaded")
    # db_mem.backup(db_disk) # write db to disk
    return app

app = create_app()

@app.route("/")
def hello_world():
    print('Hello world')    
    return "<p>Hello, World!</p>"

@app.route("/api/")
def api():
    return "<p>API Handle</p>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=10001)
