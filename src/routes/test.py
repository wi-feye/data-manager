from src import app


@app.route("/api/")
def hello():
    return "<p>Hello, World!</p>"


@app.route("/api/test/")
def test():
    return "<p>Test</p>"


@app.route("/api/api/")
def api():
    return "<p>API</p>"
