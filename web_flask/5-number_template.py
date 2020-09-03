#!/usr/bin/python3
"""
create element with template html
"""

from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def start_app():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB!'


@app.route('/c/<var>', strict_slashes=False)
def path(var):
    return 'C %s' % escape(var.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyis(text="is cool"):
    return 'Python %s' % escape(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_num(n):
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_n(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
