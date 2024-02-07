#!/usr/bin/env python3
"""Create a get_locale function with the babel.localeselector
decorator. Use request.accept_languages to determine the best
match with our supported languages."""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from typing import Union

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """class congig"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app.config.from_object(Config)


def get_user():
    """This is for get user"""
    try:
        return users.get(int(request.args.get("login_as")))
    except Exception:
        return None


@app.route("/")
def index():
    """home page"""
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """To Determines supported languages """
    if 'locale' in request.args:
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """This before function"""
    g.user = get_user()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
