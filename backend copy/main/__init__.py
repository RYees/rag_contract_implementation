from flask import jsonify

from ragbackend.main.api import api
from ragbackend.main import routes


def init_app(app):
    api.init_app(app)
