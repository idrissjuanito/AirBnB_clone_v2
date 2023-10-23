#!/usr/bin/python3
"""
flask app for querying in templates
from airbnb project storage
"""
from models import storage, State, City
from flask import Flask, render_template

from models.engine.db_storage import DBStorage
app = Flask(__name__)


@app.teardown_appcontext
def close_db(e=None):
    """
    used for cleanup by flask
    """
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """
    renders a list of all states in jinja templates
    """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states.items())


@app.route("/states/<id>/", strict_slashes=False)
def state_by_id(id):
    """
    renders a list of all states in jinja templates
    """
    states = storage.all(State)
    return render_template("9-states.html", states=states, id=f"State.{id}")


if __name__ == "__main__":
    app.run()
