from flask import request, jsonify, current_app
from psycopg2.errors import NotNullViolation
from app.models.other_skill_model import OtherSkillModel
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from flask_jwt_extended import jwt_required, get_jwt_identity


KEYS = ['description', 'level']


@jwt_required()
def create_other_skill():
    user_identity = get_jwt_identity()
    data = request.get_json()

    try:
        for key in data:
            if data[key] == "":
                return {'Error': f'Key {key} is empty'}, 400

        data['user_id'] = user_identity['id']

        skill = OtherSkillModel(**data)

        session = current_app.db.session
        session.add(skill)
        session.commit()

        return jsonify(skill), 201
    except TypeError as a:
        invalid_keys = a.args[0].split(' ')[0].strip("'")

        return {
            'invalid_keys': invalid_keys,
            'Keys': KEYS
        }, 401
    except InvalidRequestError as a:
        invalid_keys = a.args[0]

        return {
            'invalid_keys': f'The key {invalid_keys} not found',
            'valid_keys': KEYS
        }, 401
    except IntegrityError as e:

        if type(e.orig) == NotNullViolation:
            doble_quote = '"'
            single_quote = "'"
            invalid_key = e.args[0].split(' ')[5].replace(doble_quote, single_quote)
            return {'msg': f'Key {invalid_key} not found'}, 400


@jwt_required()
def get_others_skills_by_user():
    user = get_jwt_identity()
    user_identity = user['id']

    skills = OtherSkillModel.query.filter(OtherSkillModel.user_id == user_identity).all()

    return jsonify(skills), 200


@jwt_required()
def get_by_other_skill(description_like, level_like):

    skills = OtherSkillModel.query.filter(
            (OtherSkillModel.description == description_like), (OtherSkillModel.level == level_like)
        ).all()

    return jsonify(skills)


@jwt_required()
def update_other_skill(skill_id):
    session = current_app.db.session

    user = get_jwt_identity()
    user_identity = user['id']

    data = request.get_json()

    try:
        is_updated = OtherSkillModel.query.filter(
            (OtherSkillModel.user_id == user_identity), (OtherSkillModel.id == skill_id)
        ).update(data)

        if not bool(is_updated):
            return {"msg": "Skill not found"}, 404

        session.commit()

        output_update = OtherSkillModel.query.filter(
            (OtherSkillModel.user_id == user_identity), (OtherSkillModel.id == skill_id)
        ).first()

        return {"Update": output_update}, 200

    except TypeError as a:
        invalid_keys = a.args[0].split(' ')[0].strip("'")

        return {
            'invalid_keys': invalid_keys,
            'Keys': KEYS
        }
    except InvalidRequestError as a:
        invalid_keys = a.args[0].split(' ')[-1].strip("'").replace('"', "")

        return {
            'invalid_keys': f'The key {invalid_keys} not found',
            'valid_keys': KEYS
        }, 401


@jwt_required()
def delete_other_skill(skill_id):
    skill = OtherSkillModel.query.get(skill_id)

    if not skill:
        return {"Error": "Skill not found"}, 404

    OtherSkillModel.query.filter(OtherSkillModel.id == skill_id).delete()

    current_app.db.session.commit()

    return jsonify({'msg': "Skill deleted"}), 204
