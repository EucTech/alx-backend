#!/usr/bin/env python3
"""Create a single / route and an index.html template
that simply outputs “Welcome to Holberton” as page title
(<title>) and “Hello world” as header (<h1>)."""

from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    title = "Welcome to Holberton"
    return render_template("0-index.html", title=title)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
