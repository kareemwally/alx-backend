#!/usr/bin/env python3
"""
routes
"""
from flask import render_template, Flask
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
    configuring the languagaes
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index() -> None:
    """
    returning the 1-html page
    """
    return render_template("1-index.html",
                           title='Welcome to Holberton',
                           body="Hello world")


if __name__ == "__main__":
    app.run(debug=True)
