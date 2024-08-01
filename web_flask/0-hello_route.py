#!/usr/bin/python3
""" This will start up the flask webb app 
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_flask():
    """this function will return a string
    to the brower page.
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
