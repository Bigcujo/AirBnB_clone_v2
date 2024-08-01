#!/usr/bin/python3
"""Runs a flaks app what will return 
two differnt strings in to different page
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """this rouute will return the string hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """this route will return a string HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
