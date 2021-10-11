from flask import request, jsonify, current_app
from app.models.user_model import UserModel
from flask_jwt_extended import create_access_token, jwt_required


def create_user():
    session = current_app.db.session

    data = request.get_json()

    password_to_hash = data.pop('password_hash')

    new_user = UserModel(**data)

    new_user.password = password_to_hash

    session.add(new_user)
    session.commit()

    return jsonify(new_user), 201


def login():
    data = request.get_json()

    found_user: UserModel = UserModel.query.filter_by(email=data['email']).first()

    if not found_user:
        return {'error': 'User not found!'}, 404

    if found_user.verify_password(data['password_hash']):
        access_token = create_access_token(identity=found_user)

        return{
            'message': 'Success Login',
            'token_bearer': access_token
        }, 200

    else:
        return {'error': 'Unauthorized'}, 401


def update_user():
    ...


@jwt_required()
def get_user(id: int):
    user = UserModel.query.get(id)

    if not user:
        return {'message': 'User not founded!'}, 404

    return jsonify(user), 200


def delete_user():
    ...
