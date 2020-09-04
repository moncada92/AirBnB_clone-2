#!/usr/bin/python3
"""
filters airbnb
"""

from flask import Flask, escape, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(self):
    """Closes sessions"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def listStateId():
    places = storage.all(Place).values()
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    result = {}

    for p, u in storage._DBStorage__session.query(Place, User).\
            filter(Place.user_id == User.id):
        result[p.user_id] = "{} {}".format(u.first_name, u.last_name)

    return render_template('100-hbnb.html', **locals())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
