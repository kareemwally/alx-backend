#!/usr/bin/env python3
"""
routes
"""
from flask import render_template, Flask, request
from flask_babel import Babel


def get_locale() -> None:
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)


class Config:
    """
    configuring the languagaes
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index() -> None:
    """
    returning the 1-html page
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(debug=True)
