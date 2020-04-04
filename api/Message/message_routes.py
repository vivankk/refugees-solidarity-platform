from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from api import db
from api.Message.message_model import Message
from api.Tag.tag_model import Tag

messages = Blueprint("messages", __name__)


@messages.route("/messages", methods=["GET"])
def get_all_messages():
    all_messages = Message.query.all()
    serialized_data = []
    for message in all_messages:
        serialized_data.append(message.serialize)

    return jsonify({"all_messages": serialized_data})


@messages.route("/messages/<int:user_id>", methods=["GET"])
def get_all_user_messages(user_id):
    user_messages = Message.query.filter_by(user_id=user_id).all()
    serialized_data = []
    for message in user_messages:
        serialized_data.append(message.serialize)

    return jsonify({"all_messages": serialized_data})


@messages.route("/message/<int:id>", methods=["GET"])
def get_single_message(id):
    message = Message.query.filter_by(id=id).first_or_404()
    serialized_message = message.serialize
    serialized_message["tags"] = []

    for tag in message.tags:
        serialized_message["tags"].append(tag.serialize)

    return jsonify({"single_message": serialized_message})


@messages.route("/delete_message/<int:id>", methods=["DELETE"])
@jwt_required
def delete_message(id):
    message = Message.query.filter_by(id=id).first()
    db.session.delete(message)
    db.session.commit()

    return jsonify("Message was deleted"), 200


@messages.route("/update_message/<int:id>", methods=["PUT"])
@jwt_required
def update_message(id):
    data = request.get_json()
    message = Message.query.filter_by(id=id).first_or_404()

    message.title = data["title"]
    message.content = data["content"]
    message.feature_image = data["feature_image"]

    updated_message = message.serialize

    db.session.commit()
    return jsonify({"message_id": message.id})


@messages.route("/add_message", methods=["POST"])
@jwt_required
def create_message():
    data = request.get_json()

    new_message = Message(
        title=data["title"],
        content=data["content"],
        feature_image=data["feature_image"],
    )

    for tag in data["tags"]:
        present_tag = Tag.query.filter_by(name=tag).first()
        if present_tag:
            present_tag.messages_associated.append(new_message)
        else:
            new_tag = Tag(name=tag)
            new_tag.messages_associated.append(new_message)
            db.session.add(new_tag)

    db.session.add(new_message)
    db.session.commit()

    msg_id = getattr(new_message, "id")
    return jsonify({"id": msg_id})
