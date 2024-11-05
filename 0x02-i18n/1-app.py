#!/usr/bin/env python3
"""
routes
"""
from flask import Flask
from flask import render_template
from flask_babel import Babel


def get_locale():
    """
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)


class Config:
    """
    the main class for languages
    """
    LANGUAGES = ['en', 'fr']
