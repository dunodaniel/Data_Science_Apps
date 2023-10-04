"""
This module contains a Flask application.
"""

from flask import Flask



app = Flask(__name__)

@app.route("/")
def hello_world():
    """
    Returns a simple message to the user.
    """
    return "<p>Hello, World!</p>\n"
