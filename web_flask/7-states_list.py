#!/usr/bin/python3

from models import storage
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    s = storage.all(State).values()
    return render_template("7-states_list.html", states=s)


@app.teardown_appcontext
def tear(self):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)