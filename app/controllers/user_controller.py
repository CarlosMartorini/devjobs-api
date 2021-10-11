from flask import request, jsonify, current_app
from app.models.user_model import UserModel
from flask_jwt_extended import create_access_token


def create_user():
    session = current_app.db.session

    data = request.get_json()

    new_user = UserModel(**data)

    session.add(new_user)
    session.commit()

    return jsonify(new_user), 201


def login():
    data = request.get_json()

    found_user: UserModel = UserModel.query.filter_by(email=data['email']).first()

    if not found_user:
        return {'error': 'User not found!'}, 404

    if found_user.verify_password(data['password']):
        access_token = create_access_token(identity=found_user)

        return{
            'message': 'Success Login',
            'token_bearer': access_token
        }, 200

    else:
        return {'error': 'Unauthorized'}, 401


def update_user():
    ...


def get_user(id: int):
    user = UserModel.query.get(id)

    return jsonify(user), 200


def delete_user():
    ...
