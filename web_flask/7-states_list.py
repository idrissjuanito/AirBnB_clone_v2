#!/usr/bin/python3
"""
flask app for querying a list of states
from airbnb project storage
"""
from models import storage, State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_db(e=None):
    """
    used for cleanup by flask
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def get_states():
    """
    queries storage for states and renders with jinja template
    """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states.items())


if __name__ == "__main__":
    app.run()
