from flask import request, jsonify, current_app
from app.models.summary_model import SummaryModel
from flask_jwt_extended import jwt_required, get_jwt_identity


VALID_KEYS = [
    'objective',
    'city',
    'speciality',
    'disponibility',
    'experience_time',
    'user_id'
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
        }


@jwt_required()
def update_summary():
    session = current_app.db.session

    try:
        data = request.get_json()

        summary = get_jwt_identity()

        SummaryModel.query.filter(SummaryModel.id == summary['id']).update(data)

        session.commit()

        updated_summary = get_jwt_identity()

        if not updated_summary:
            return {'error': 'Summary not found!'}, 404

        return {'summary_update': updated_summary}, 200

    except TypeError as e:
        invalid_key = e.args[0].split(' ')[0].strip("'")

        return {
            'invalid_key': invalid_key,
            'valid_keys': VALID_KEYS
        }


@jwt_required()
def get_summary():
    user = get_jwt_identity()

    summary = SummaryModel.query.filter_by(user_id=user['id']).first()

    if not summary:
        return {'error': 'Summary not found!'}, 404

    return {'summary': summary}, 200


def delete_summary():
    ...
