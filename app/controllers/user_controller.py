from flask import request, jsonify, current_app
from app.models.user_model import UserModel


def create_user():
    session = current_app.db.session

    data = request.get_json()

    new_user = UserModel(**data)

    session.add(new_user)
    session.commit()

    return jsonify(new_user), 201


def login():
    ...


def update_user():
    ...


def get_user(id: int):
    user = UserModel.query.get(id)

    return jsonify(user), 200


def delete_user():
    ...
