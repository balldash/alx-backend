#!/usr/bin/env python3
"""
A Flask app with babel configuration.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
    The Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)


@app.route("/", methods=["GET"], strict_slashes=False)
def home():
    """
    The home route
    return: The index template
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
