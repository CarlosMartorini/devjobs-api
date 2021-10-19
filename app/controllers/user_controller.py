from flask import request, jsonify, current_app
from app.models.user_model import UserModel
from flask_jwt_extended import create_access_token, jwt_required
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation, NotNullViolation


VALID_KEYS = [
    'email',
    'password',
    'firstName',
    'lastName',
    'birthDate',
    'linkedinProfile',
    'address',
    'phone'
]

LOGIN_KEYS = ['email', 'password']


def create_user():
    try:
        session = current_app.db.session

        data = request.get_json()

        for item in data:
            if data[item] == "":
                return {'msg': f'Key {item} is empty!'}, 400

        password_to_hash = data.pop('password')

        new_user = UserModel(**data)

        new_user.password = password_to_hash

        session.add(new_user)
        session.commit()

        return jsonify(new_user), 201

    except IntegrityError as e:
        if type(e.orig) == UniqueViolation:
            return {'msg': 'Email already exists!'}, 409

        if type(e.orig) == NotNullViolation:
            invalid_keys = e.args[0].split(' ')[5].replace('"', "'")

            return {'msg': f'Key {invalid_keys} not found'}, 400

    except TypeError as e:
        invalid_key = e.args[0].split(' ')[0].strip("'")

        return {
            'invalid_keys': invalid_key,
            'valid_keys': VALID_KEYS
        }, 400


def login():
    try:
        data = request.get_json()

        for item in data:
            if data[item] == "":
                return {'msg': f'Key {item} is empty!'}, 400

        found_user: UserModel = UserModel.query.filter_by(email=data['email']).first()

        if not found_user:
            return {'msg': 'User not found!'}, 404

        if found_user.verify_password(data['password']):
            access_token = create_access_token(identity=found_user)

            return {
                'accessToken': access_token
            }, 200

        else:
            return {'msg': 'Unauthorized'}, 401

    except KeyError as e:
        invalid_keys = e.args[0]

        return {
            'invalid_keys': f'The key {invalid_keys} not found',
            'valid_keys': LOGIN_KEYS
        }, 400


def update_user():
    ...


@jwt_required()
def get_user(id: int):
    user = UserModel.query.get(id)

    if not user:
        return {'msg': 'User not founded!'}, 404

    return jsonify(user), 200


def delete_user():
    ...
