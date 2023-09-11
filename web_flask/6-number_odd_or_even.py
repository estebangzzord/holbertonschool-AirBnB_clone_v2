#!/usr/bin/python3
"""
Starts a Flask web application.
"""


from flask import Flask, render_template
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


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Displays an html page if n is an integer """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ Displays an html page that tells if a number is even or odd """
    if n % 2 == 0:
        evenness = 'even'
    else:
        evenness = 'odd'

    return render_template('6-number_odd_or_even.html', n=n, evenness=evenness)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
