#!/usr/bin/python3
"""
New view for Amenity objects that handles all default RESTFul API actions
"""

from flask import request
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'])
def get_amenity():
    amenities = [amenity.to_dict()
                 for amenity in storage.all(Amenity).values()]
    return jsonify(amenities)


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenityId(amenity_id):
    instance = storage.get(Amenity, amenity_id)

    if instance is None:
        return jsonify({"error": "Not found"}), 404

    return jsonify(instance.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def del_amenity(amenity_id):
    instance = storage.get(Amenity, amenity_id)

    if instance is None:
        return jsonify({"error": "Not found"}), 404

    storage.delete(instance)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'])
def create_amenity():
    json_data = request.get_json()

    if json_data is None:
        return jsonify({"error": "Not found"}), 400

    if "name" not in json_data:
        return jsonify({"error": "Missing name"}), 400

    new_instance = Amenity(**json_data)
    storage.new(new_instance)
    storage.save()
    return jsonify(new_instance.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    instance = storage.get(Amenity, amenity_id)
    json_data = request.get_json()

    if instance is None:
        return jsonify({"error": "Not found"}), 404

    if json_data is None:
        return jsonify({"error": "Not a JSON"}), 400

    for key, value in json_data.items():
        setattr(instance, key, value)
    storage.save()

    return jsonify(instance.to_dict()), 200
