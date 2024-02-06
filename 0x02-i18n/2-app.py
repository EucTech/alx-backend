#!/usr/bin/env python3
"""Create a get_locale function with the babel.localeselector
decorator. Use request.accept_languages to determine the best
match with our supported languages."""

import babel
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
Babel = Babel(app)


class Config(object):
    """class congig"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('2-app.Config')


@app.route("/")
def index() -> str:
    """home page"""
    return render_template("2-index.html")


@babel.localeselector
def get_locale() -> str:
    """To Determines supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
