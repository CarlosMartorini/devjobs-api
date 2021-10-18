from flask import request, jsonify, current_app
from app.models.tech_skill_model import TechSkillModel
from sqlalchemy.exc import InvalidRequestError, NoResultFound
from flask_jwt_extended import jwt_required, get_jwt_identity


KEYS = [
    'description',
    'level'
]


@jwt_required()
def create_skill():
    user_identity = get_jwt_identity()
    data = request.get_json()

    try:
        for key in data:
            if data[key] == "":
                return {'Error': f'Key {key} is empty'}, 400

        data['user_id'] = user_identity['id']

        skill = TechSkillModel(**data)

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


@jwt_required()
def get_skills_by_userId():
    user = get_jwt_identity()
    user_identity = user['id']

    try:
        skills = TechSkillModel.query.filter(TechSkillModel.user_id == user_identity).all()

    except NoResultFound:
        return {"Error": "User Not in Database"}, 404

    return jsonify(skills), 200


@jwt_required()
def get_users_by_one_skill(description_like, level_like):

    try:
        skills = TechSkillModel.query.filter(
                TechSkillModel.description == description_like, TechSkillModel.level == level_like
            ).all()

    except NoResultFound:
        return {"Error": "Description or Level Not in Database"}, 404

    return jsonify(skills)


@jwt_required()
def update_skill(skill_id):
    session = current_app.db.session

    user = get_jwt_identity()
    user_identity = user['id']

    data = request.get_json()

    try:
        TechSkillModel.query.filter(
            TechSkillModel.user_id == user_identity,
            TechSkillModel.id == skill_id).update(data)

        session.commit()

        output_update = TechSkillModel.query.filter(
            TechSkillModel.user_id == user_identity,
            TechSkillModel.id == skill_id).first()

        return {"Update": output_update}

    except TypeError as a:
        invalid_keys = a.args[0].split(' ')[0].strip("'")

        return {
            'invalid_keys': invalid_keys,
            'Keys': KEYS
        }
    except InvalidRequestError as a:
        invalid_keys = a.args[0]

        return {
            'invalid_keys': f'The key {invalid_keys} not found',
            'valid_keys': KEYS
        }, 401


@jwt_required()
def delete_skill(skill_id):
    skill = TechSkillModel.query.get(skill_id)

    if not skill:
        return {"Error": "Skill not found"}, 404

    TechSkillModel.query.filter(TechSkillModel.id == skill_id).delete()

    current_app.db.session.commit()

    return jsonify({'msg': "Skill deleted"}), 204
