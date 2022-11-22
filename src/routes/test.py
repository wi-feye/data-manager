from src import app

from flask import request

@app.route("/api/")
def hello():
    return "<p>API Handle</p>"


@app.route("/api/query") # /api/query?name=Test
def test_query():
    name = request.args.get("name")
    return f'<p>name={name}</p>'
