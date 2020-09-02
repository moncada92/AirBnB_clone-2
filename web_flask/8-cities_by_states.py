#!/usr/bin/python3
"""
get data states and cities airbnb
"""

from flask import Flask, escape, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(self):
    """Closes sessions"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def listCities():
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
