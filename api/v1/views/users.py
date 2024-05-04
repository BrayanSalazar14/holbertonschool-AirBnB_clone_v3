#!/usr/bin/python3
"""
New view for User objects that handles all default RESTFul API actions
"""

from flask import request
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'])
def get_users():
    users = [users.to_dict()
             for users in storage.all(User).values()]
    return jsonify(users)


@app_views.route('/users/<user_id>', methods=['GET'])
def get_usersId(user_id):
    instance = storage.get(User, user_id)

    if instance is None:
        return jsonify({"error": "Not found"}), 404

    return jsonify(instance.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'])
def del_user(user_id):
    instance = storage.get(User, user_id)

    if instance is None:
        return jsonify({"error": "Not found"}), 404

    storage.delete(instance)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'])
def create_user():
    json_data = request.get_json()

    if json_data is None:
        return jsonify({"error": "Not found"}), 400

    if "email" not in json_data:
        return jsonify({"error": "Missing email"}), 400

    if "password" not in json_data:
        return jsonify({"error": "Missing password"}), 400

    new_instance = User(**json_data)
    storage.new(new_instance)
    storage.save()
    return jsonify(new_instance.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'])
def update_users(user_id):
    instance = storage.get(User, user_id)
    json_data = request.get_json()

    if instance is None:
        return jsonify({"error": "Not found"}), 404

    if json_data is None:
        return jsonify({"error": "Not a JSON"}), 400

    for key, value in json_data.items():
        setattr(instance, key, value)
    storage.save()

    return jsonify(instance.to_dict()), 200
