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
from models.review import Review


@app_views.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = [review.to_dict() for review in storage.all(Review).values()]
    return jsonify(reviews)


@app_views.route('/places/<place_id>/reviews', methods=['GET'])
def get_review(place_id):
    place = storage.get(Place, place_id)

    if place is None:
        return jsonify({"error": "Not found"}), 404

    reviews = [review.to_dict()
               for review in storage.all(Review).values() if review.place_id == place.id]

    return jsonify(reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'])
def get_reviewId(review_id):
    instance = storage.get(Review, review_id)

    if instance is None:
        return jsonify({"error": "Not found"}), 404

    return jsonify(instance.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'])
def del_review(review_id):
    instance = storage.get(Review, review_id)

    if instance is None:
        return jsonify({"error": "Not found"}), 404

    storage.delete(instance)
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews', methods=['POST'])
def create_review(place_id):
    json_data = request.get_json()
    place = storage.get(Place, place_id)

    if json_data is None:
        return jsonify({"error": "Not found"}), 400

    if place is None:
        return jsonify({"error": "Not found"}), 404

    if "user_id" not in json_data:
        return jsonify({"error": "Missing user_id"}), 400

    user = storage.get(User, json_data['user_id'])

    if user is None:
        return jsonify({"error": "Not found"}), 404

    if "text" not in json_data:
        return jsonify({"error": " Missing text"}), 400

    json_data.update({"place_id": place.id})
    new_instance = Review(**json_data)
    storage.new(new_instance)
    storage.save()
    return jsonify(new_instance.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    instance = storage.get(Review, review_id)
    json_data = request.get_json()

    if instance is None:
        return jsonify({"error": "Not found"}), 404

    if json_data is None:
        return jsonify({"error": "Not a JSON"}), 400

    for key, value in json_data.items():
        setattr(instance, key, value)
    storage.save()

    return jsonify(instance.to_dict()), 200
