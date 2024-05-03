#!/usr/bin/python3
"""
Module that return the status as a Json file
"""


from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    return jsonify({"status": "OK"})
