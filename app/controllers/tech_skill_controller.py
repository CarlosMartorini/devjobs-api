from flask import request, jsonify, current_app
from psycopg2.errors import NotNullViolation
from app.models.tech_skill_model import TechSkillModel
from sqlalchemy.exc import IntegrityError, InvalidRequestError, NoResultFound
from flask_jwt_extended import jwt_required


KEYS = [
    'description',
    'level'
]


@jwt_required()
def create_skill():
    user_id = request.args.get('userId')
    if not user_id:
        return {"msg": "Argument userId is required"}, 400

    data = request.get_json()
    data['user_id'] = int(user_id)

    try:
        for key in data:
            if data[key] == "":
                return {'msg': f'Key {key} is empty'}, 400

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
def get_skills_by_userId():
    user_id = request.args.get('userId')
    if not user_id:
        return {"msg": "Argument userId is required"}, 400

    try:
        skills = TechSkillModel.query.filter(TechSkillModel.user_id == int(user_id)).all()

    except NoResultFound:
        return {"msg": "User Not in Database"}, 404

    return jsonify(skills), 200


@jwt_required()
def get_users_by_one_skill(description_like, level_like):

    try:
        skills = TechSkillModel.query.filter(
                TechSkillModel.description == description_like, TechSkillModel.level == level_like
            ).all()

    except NoResultFound:
        return {"msg": "Description or Level Not in Database"}, 404

    return jsonify(skills)


@jwt_required()
def update_skill(skill_id):
    session = current_app.db.session

    user_id = request.args.get('userId')
    if not user_id:
        return {"msg": "Argument userId is required"}, 400

    data = request.get_json()

    try:
        is_updated = TechSkillModel.query.filter(
            TechSkillModel.user_id == int(user_id),
            TechSkillModel.id == skill_id).update(data)

        if not bool(is_updated):
            return {"msg": "Skill not found"}, 404

        session.commit()

        output_update = TechSkillModel.query.filter(
            TechSkillModel.user_id == int(user_id),
            TechSkillModel.id == skill_id).first()

        return jsonify(output_update)

    except TypeError as e:
        invalid_keys = e.args[0].split(' ')[0].strip("'")

        return {
            'invalid_keys': invalid_keys,
            'Keys': KEYS
        }
    except InvalidRequestError as e:
        doble_quote = '"'
        invalid_key = e.args[0].split(' ')[-1].replace(doble_quote, '')
        return {
            'invalid_keys': {invalid_key},
            'valid_keys': KEYS
        }, 401


@jwt_required()
def delete_skill(skill_id):
    skill = TechSkillModel.query.get(skill_id)

    if not skill:
        return {"msg": "Skill not found"}, 404

    TechSkillModel.query.filter(TechSkillModel.id == skill_id).delete()

    current_app.db.session.commit()

    return {'msg': "Skill deleted"}, 204
