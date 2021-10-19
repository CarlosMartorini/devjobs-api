from flask import request, jsonify, current_app
from psycopg2.errors import NotNullViolation
from app.models.other_skill_model import OtherSkillModel
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from flask_jwt_extended import jwt_required


KEYS = ['description', 'level']


@jwt_required()
def create_other_skill():
    user_id = request.args.get('userId')
    if not user_id:
        return {"msg": "Argument userId is required"}, 400

    data = request.get_json()
    data['user_id'] = int(user_id)

    try:
        for key in data:
            if data[key] == "":
                return {'msg': f'Key {key} is empty'}, 400

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
        }, 400

    except InvalidRequestError as a:
        invalid_keys = a.args[0]

        return {
            'invalid_keys': f'The key {invalid_keys} not found',
            'valid_keys': KEYS
        }, 400

    except IntegrityError as e:

        if type(e.orig) == NotNullViolation:
            doble_quote = '"'
            single_quote = "'"
            invalid_key = e.args[0].split(' ')[5].replace(doble_quote, single_quote)
            return {'msg': f'Key {invalid_key} not found'}, 400


@jwt_required()
def get_others_skills_by_user():
    user_id = request.args.get('userId')
    if not user_id:
        return {"msg": "Argument userId is required"}, 400

    skills = OtherSkillModel.query.filter(OtherSkillModel.user_id == int(user_id)).all()

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

    user_id = request.args.get('userId')
    if not user_id:
        return {"msg": "Argument userId is required"}, 400

    data = request.get_json()

    try:
        is_updated = OtherSkillModel.query.filter(
            (OtherSkillModel.user_id == int(user_id)), (OtherSkillModel.id == skill_id)
        ).update(data)

        if not bool(is_updated):
            return {"msg": "Skill not found"}, 404

        session.commit()

        output_update = OtherSkillModel.query.filter(
            (OtherSkillModel.user_id == int(user_id)), (OtherSkillModel.id == skill_id)
        ).first()

        return jsonify(output_update), 200

    except TypeError as a:
        invalid_keys = a.args[0].split(' ')[0].strip("'")

        return {
            'invalid_keys': invalid_keys,
            'valid_keys': KEYS
        }
    except InvalidRequestError as a:
        invalid_keys = a.args[0].split(' ')[-1].strip("'").replace('"', "")

        return {
            'invalid_key': invalid_keys,
            'valid_keys': KEYS
        }, 401


@jwt_required()
def delete_other_skill(skill_id):
    skill = OtherSkillModel.query.get(skill_id)

    if not skill:
        return {"msg": "Skill not found"}, 404

    OtherSkillModel.query.filter(OtherSkillModel.id == skill_id).delete()

    current_app.db.session.commit()

    return jsonify({'msg': "Skill deleted"}), 204
