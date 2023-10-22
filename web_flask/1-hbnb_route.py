#!/usr/bin/python3
""" Basic flask app with routes """
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """
    Home route handler
    renders a string
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    route to display another string
    """
    return "HBNB"


if __name__ == "__main__":
    app.run()
