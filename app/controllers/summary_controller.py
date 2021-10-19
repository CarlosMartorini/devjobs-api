from flask import request, jsonify, current_app
from psycopg2.errors import NotNullViolation, UniqueViolation
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from app.models.summary_model import SummaryModel
from flask_jwt_extended import jwt_required


VALID_KEYS = [
    'objective',
    'city',
    'speciality',
    'disponibility',
    'experienceTime',
]


@jwt_required()
def create_summary():
    session = current_app.db.session

    try:
        user_id = request.args.get('userId')

        if not user_id:
            return {"msg": "Argument userId is required"}, 400

        data = request.get_json()

        for item in data:
            if data[item] == "":
                return {'msg': f'Key {item} is empty!'}, 400

        data['user_id'] = int(user_id)

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

        if type(e.orig) == UniqueViolation:
            return {"msg": f"User with id {user_id} already have a summary"}, 409


@jwt_required()
def update_summary():
    session = current_app.db.session

    try:
        data = request.get_json()

        user_id = request.args.get('userId')

        if not user_id:
            return {"msg": "Argument userId is required"}, 400

        SummaryModel.query.filter(SummaryModel.user_id == int(user_id)).update(data)

        session.commit()

        output_summary = SummaryModel.query.filter_by(user_id=int(user_id)).first()

        return jsonify(output_summary), 200

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
    user_id = int(request.args.get('userId'))

    summary = SummaryModel.query.filter_by(user_id=user_id).first()

    if not summary:
        return {'msg': 'Summary not found!'}, 404

    return jsonify(summary), 200


def delete_summary():
    ...
