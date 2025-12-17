import flask

app = flask.Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)

@app.get("/")
def index():
    return flask.send_from_directory("static", "index.html")

if __name__ == "__main__":
    app.run()