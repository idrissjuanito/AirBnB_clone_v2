#!/usr/bin/python3
"""
flask app for querying in templates
from airbnb project storage
"""
from models import storage, State, City
from flask import Flask, render_template
from models.amenity import Amenity

from models.engine.db_storage import DBStorage
app = Flask(__name__)


@app.teardown_appcontext
def close_db(e=None):
    """
    used for cleanup by flask
    """
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def states():
    """
    renders airbnb static pages
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html",
                           states=states.items(),
                           amenities=amenities.items())


if __name__ == "__main__":
    app.run()
