#!/usr/bin/env python3
"""
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)


class Config:
    """Config class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> None:
    """Determine the best match for supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> None:
    """Route for index page"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
