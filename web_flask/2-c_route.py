#!usr/bin/env python3
"""
create second route with variables
"""

from flask import Flask, escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def start_app():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB!'


@app.route('/c/<string:var>')
def path(var):
    return 'C %s' % escape(var.replace('_',' '))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
