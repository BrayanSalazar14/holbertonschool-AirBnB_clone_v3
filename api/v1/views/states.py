#!/usr/bin/python3
"""
New view for State objects that handles all default RESTFul API actions
"""

from flask import request
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
    storage.save()
    return {}, 200


@app_views.route('/states', methods=['POST'])
def process_json():
    json_data = request.get_json()

    if json_data is None:
        return jsonify({"error": "Not found"}), 400

    if "name" not in json_data:
        return jsonify({"error": "Missing name"}), 400

    new_instance = State(**json_data)
    storage.new(new_instance)
    storage.save()
    return jsonify(new_instance.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_obj(state_id):
    instance = storage.get(State, state_id)
    json_data = request.get_json()

    if instance is None:
        return jsonify({"error": "Not found"}), 404

    if json_data is None:
        return jsonify({"error": "Not a JSON"}), 400

    for key, value in json_data.items():
        setattr(instance, key, value)
    storage.save()

    return jsonify(instance.to_dict()), 200
