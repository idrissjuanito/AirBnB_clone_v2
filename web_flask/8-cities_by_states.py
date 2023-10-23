#!/usr/bin/python3
"""
flask app for querying a list of cities by state
from airbnb project storage
"""
from models import storage, State, City
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_db(e=None):
    """
    used for cleanup by flask
    """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def get_states():
    """
    queries storage for cities and renders with jinja template
    """
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states.items())


if __name__ == "__main__":
    app.run()
