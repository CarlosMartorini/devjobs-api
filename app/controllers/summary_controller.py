from flask import request, jsonify, current_app
from psycopg2.errors import NotNullViolation
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from app.models.summary_model import SummaryModel
from flask_jwt_extended import jwt_required, get_jwt_identity


VALID_KEYS = [
    'objective',
    'city',
    'speciality',
    'disponibility',
    'experience_time',
]


@jwt_required()
def create_summary():
    session = current_app.db.session

    try:
        user = get_jwt_identity()

        data = request.get_json()

        for item in data:
            if data[item] == "":
                return {'error': f'Key {item} is empty!'}, 400

        data['user_id'] = user['id']

        new_summary = SummaryModel(**data)

        session.add(new_summary)
        session.commit()

        return jsonify(new_summary), 201

    except TypeError as e:
        invalid_key = e.args[0].split(' ')[0].strip("'")

        return {
            'invalid_key': invalid_key,
            'valid_keys': VALID_KEYS
        }, 400

    except IntegrityError as e:

        if type(e.orig) == NotNullViolation:
            doble_quote = '"'
            single_quote = "'"
            invalid_key = e.args[0].split(' ')[5].replace(doble_quote, single_quote)
            return {'msg': f'Key {invalid_key} not found'}, 400


@jwt_required()
def update_summary():
    session = current_app.db.session

    try:
        data = request.get_json()

        user = get_jwt_identity()

        SummaryModel.query.filter(SummaryModel.user_id == user['id']).update(data)

        session.commit()

        output_summary = SummaryModel.query.filter_by(user_id=user['id']).first()

        return {'summary_update': output_summary}, 200

    except TypeError as e:
        invalid_key = e.args[0].split(' ')[0].strip("'")

        return {
            'invalid_key': invalid_key,
            'valid_keys': VALID_KEYS
        }, 400
    except InvalidRequestError as e:
        doble_quote = '"'
        invalid_key = e.args[0].split(' ')[-1].replace(doble_quote, '')
        return {
            'invalid_key': invalid_key,
            'valid_keys': VALID_KEYS
        }, 400


@jwt_required()
def get_summary():
    user = get_jwt_identity()

    summary = SummaryModel.query.filter_by(user_id=user['id']).first()

    if not summary:
        return {'error': 'Summary not found!'}, 404

    return {'summary': summary}, 200


def delete_summary():
    ...
