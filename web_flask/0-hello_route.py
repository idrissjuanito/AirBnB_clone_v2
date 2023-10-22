#!/usr/bin/python3
""" creates and runs a minimal flask app """
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    """ Root root of the app """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
