#!/usr/bin/python3
"""
Starts a Flask web application.
"""


from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Displays some text """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Displays some more text """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ Displays even more text """
    return "C " + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text='is cool'):
    """ Displays some more text """
    return "Python " + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if n is an integer."""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
