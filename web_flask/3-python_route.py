#!/usr/bin/python3
"""Starts th web application with 4 routing and it will run on host '0.0.0.0' on port 5000
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Return the string Hello HBNB! when this route is queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return the string HBNB when this route is quried
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Return concatinated c and thentext variable
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """Returns two routes with a varable text or without it
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
