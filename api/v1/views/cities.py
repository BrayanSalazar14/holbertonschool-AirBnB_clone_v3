#!/usr/bin/python3
"""
New view for Cities objects that handles all default RESTFul API actions
"""

from flask import request
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City


@app_views.route('/cities', methods=['GET'])
def get_city():
    city = [city.to_dict() for city in storage.all(City).values()]
    return jsonify(city)


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def get_cityId(state_id):
    instance_state = storage.get(State, state_id)
    instance_cities = storage.all(City)

    if instance_state is None:
        return jsonify({"error": "Not found"}), 404

    list_combined = [
        city.to_dict() for city in instance_cities.values()
        if city.state_id == instance_state.id]

    return jsonify(list_combined)


@ app_views.route('/cities/<city_id>', methods=['GET'])
def getCity(city_id):
    instance = storage.get(City, city_id)

    if instance is None:
        return jsonify({"error": "Not found"}), 404

    return jsonify(instance.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def del_city(city_id):
    instance = storage.get(City, city_id)

    if instance is None:
        return jsonify({"error": "Not found"}), 404

    storage.delete(instance)
    storage.save()
    return jsonify({}), 200


@ app_views.route('/states/<state_id>/cities', methods=['POST'])
def create_city(state_id):
    json_data = request.get_json()

    if json_data is None:
        return jsonify({"error": "Not found"}), 400

    if "name" not in json_data:
        return jsonify({"error": "Missing name"}), 400
    
    json_data.update({'state_id':state_id})
    new_instance = City(**json_data)
    storage.new(new_instance)
    storage.save()
    return jsonify(new_instance.to_dict()), 201


@ app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    instance = storage.get(City, city_id)
    json_data = request.get_json()

    if instance is None:
        return jsonify({"error": "Not found"}), 404

    if json_data is None:
        return jsonify({"error": "Not a JSON"}), 400

    for key, value in json_data.items():
        setattr(instance, key, value)
    storage.save()

    return jsonify(instance.to_dict()), 200
