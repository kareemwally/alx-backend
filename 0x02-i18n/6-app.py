from flask import Flask, render_template, request, g
from flask_babel import Babel, _


app = Flask(__name__)


class Config:
    """Config class for Flask app"""
    LANGUAGES = ["en", "fr", "kg"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> None:
    """
    Retrieve the user from the mock database using the login_as parameter.
    Returns the user dictionary or None if the ID is
    not found or login_as was not passed.
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """
    Execute before all other functions.
    Set the user retrieved from get_user() as a global
    on flask.g.user.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> None:
    """
    Determine the best match for supported languages
    based on the following priority:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> None:
    """Route for index page"""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
