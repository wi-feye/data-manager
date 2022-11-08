from flask import Flask
import sqlite3 as sl

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    db_disk = sl.connect('db_disk.db')
    db_mem = sl.connect(':memory:')
    db_disk.backup(db_mem)
    app.run()
    # ...
    # db_mem.backup(db_disk) # write db to disk
