#!/usr/bin/env python3
"""
routes
"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    """
    returning the specified html page
    """
    return render_template("../templates/0-index.html",
                           title='Welcome to Holberton',
                           body="Hello world")
