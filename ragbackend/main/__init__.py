from flask import jsonify

from ragbackend.main.api import api

def init_app(app):
    api.init_app(app)
