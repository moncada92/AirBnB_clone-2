#!/usr/bin/python3
"""
get data states and cities for states id airbnb
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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def listStateId(id=None):
    state = None
    states = storage.all(State).values()

    if id:
        for i in states:
            if i.id == id:
                state = i

    return render_template('9-states.html', **locals())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
