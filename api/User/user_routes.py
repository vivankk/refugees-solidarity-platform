from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from api import db
from api.User.user_model import User

users = Blueprint("users", __name__)


@users.route("/users", methods=["GET"])
def get_all_users():
    all_users = User.query.all()
    serialized_data = []
    for user in all_users:
        serialized_data.append(user.serialize)

    return jsonify({"all_users": serialized_data})


@users.route("/users/<int:user_id>", methods=["GET"])
def get_single_user(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    serialized_user = user.serialize

    return jsonify({"single_user": serialized_user})


@users.route("/add_user", methods=["POST"])
@jwt_required
def add_user():
    data = request.get_json()

    new_user = User(email=data["email"], password=data["password"])

    db.session.add(new_user)
    db.session.commit()

    user_id = getattr(new_user, "id")
    return jsonify({"id": user_id})
