#!/usr/bin/python3
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'])
def get_obj():
    states = [states.to_dict() for states in storage.all(State).values()]
    return jsonify(states)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_objId(state_id):
    instance = storage.get(State, state_id)
    if instance is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(instance.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'])
def del_obj(state_id):
    instance = storage.get(State, state_id)
    if instance is None:
        return jsonify({"error": "Not found"}), 404
    storage.delete(instance)
    return jsonify({}), 200
