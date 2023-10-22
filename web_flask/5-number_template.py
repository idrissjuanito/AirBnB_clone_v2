#!/usr/bin/python3
"""
basic flask app with 5 routes
"""
from flask import Flask, render_template
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


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
def pythons(text):
    """
    compose response string with option param
    """
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def numbers(n):
    """
    response if param is integer
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    response if param is integer
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run()
