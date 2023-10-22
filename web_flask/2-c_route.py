#!/usr/bin/python3
"""
basic flask app with 3 routes
one of the routes accepts a variable
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """
    home route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ simple route to return string """
    return "HBNB"


@app.route("/c/<param>", strict_slashes=False)
def c_is_fun(param):
    """
    route display a string composed with
    """
    return f"C {param.replace('_', ' ')}"


if __name__ == "__main__":
    app.run()
