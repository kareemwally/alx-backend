#!/usr/bin/env python3
"""
routes
"""
from app import app
from flask import render_template


@app.route('/')
def index():
    """
    returning the specified html page
    """
    return  render_template("0-index.html", title='Welcome to Holberton',
                            body="Hello world")
