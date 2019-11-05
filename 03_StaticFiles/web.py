#!/usr/bin/env python3
# This example demonstrates how to serve
# static files via Flask

from flask import Flask, render_template

app = Flask(__name__)

# define here routes
@app.route('/')
def index():
    title = 'Serving static files via Flask'
    return render_template('index.html', title=title)


if __name__ == '__main__':
    # add debug = True to auto reload templates
    # during development
    app.run(debug=True)
