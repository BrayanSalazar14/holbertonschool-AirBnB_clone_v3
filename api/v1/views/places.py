#!/usr/bin/python3
"""
New view for Places objects that handles all default RESTFul API actions
"""

from flask import request
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.user import User
from models.place import Place
from models.city import City


@app_views.route('/places', methods=['GET'])
def get_places():
    places = [place.to_dict() for place in storage.all(Place).values()]
    return jsonify(places)


@app_views.route('/cities/<city_id>/places', methods=['GET'])
def get_place(city_id):
    city = storage.get(City, city_id)

    if city is None:
        return jsonify({"error": "Not found"}), 404

    places = [place.to_dict()
              for place in storage.all(Place).values() if place.city_id == city.id]

    return jsonify(places)


@app_views.route('/places/<place_id>', methods=['GET'])
def get_placeId(place_id):
    instance = storage.get(Place, place_id)

    if instance is None:
        return jsonify({"error": "Not found"}), 404

    return jsonify(instance.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'])
def del_place(place_id):
    instance = storage.get(Place, place_id)

    if instance is None:
        return jsonify({"error": "Not found"}), 404

    storage.delete(instance)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'])
def create_place(city_id):
    json_data = request.get_json()
    city = storage.get(City, city_id)

    if json_data is None:
        return jsonify({"error": "Not found"}), 400

    if city is None:
        return jsonify({"error": "Not found"}), 404

    if "user_id" not in json_data:
        return jsonify({"error": "Missing user_id"}), 400

    user = storage.get(User, json_data['user_id'])

    if user is None:
        return jsonify({"error": "Not found"}), 404

    if "name" not in json_data:
        return jsonify({"error": "Missing name"}), 400

    json_data.update({"city_id": city.id})
    new_instance = Place(**json_data)
    storage.new(new_instance)
    storage.save()
    return jsonify(new_instance.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    instance = storage.get(Place, place_id)
    json_data = request.get_json()

    if instance is None:
        return jsonify({"error": "Not found"}), 404

    if json_data is None:
        return jsonify({"error": "Not a JSON"}), 400

    for key, value in json_data.items():
        setattr(instance, key, value)
    storage.save()

    return jsonify(instance.to_dict()), 200
