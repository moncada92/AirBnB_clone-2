#!/usr/bin/python3
"""
filters airbnb
"""

from flask import Flask, escape, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(self):
    """Closes sessions"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def listStateId():
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', **locals())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
