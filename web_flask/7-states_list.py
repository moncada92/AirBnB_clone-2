#!/usr/bin/python3
"""
get data states airbnb
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


@app.route('/states_list', strict_slashes=False)
def listStates():
    data = storage.all(State).values()
    return render_template('7-states_list.html', data=data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
