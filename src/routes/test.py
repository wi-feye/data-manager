from src import app


@app.route("/")
def hello():
    return "<p>Hello, World!</p>"


@app.route("/test/")
def test():
    return "<p>Test</p>"


@app.route("/api/")
def api():
    return "<p>API</p>"
