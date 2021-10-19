from flask import jsonify, request, current_app
from app.models.experience_model import ExperienceModel as EXM
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import NoResultFound, IntegrityError
from psycopg2.errors import ForeignKeyViolation

VALID_KEYS = [
    "role",
    "company",
    "dateFrom",
    "dateTo",
    "description",
    "userId"
]


@jwt_required()
def get_experience():

    try:
        user_id = int(request.args.get('userId'))

        experience = EXM.query.filter(EXM.user_id == user_id).all()

    except NoResultFound:
        return {"msg": "User Not in Database"}, 404

    except TypeError:
        return {"msg": "Argument userId not found"}, 400

    return jsonify(experience), 200


@jwt_required()
def create_experience():

    data = request.get_json()

    try:
        data["dateFrom"]

    except KeyError:
        data["dateFrom"] = None

    try:
        data["dateTo"]

    except KeyError:
        data["dateTo"] = None

    try:
        output = EXM.create_one(data)

        return jsonify(output), 201
    except KeyError as e:
        return {
            "msg": f"Key {e.args[0]} not found",
            "valid_keys": VALID_KEYS
        }, 400

    except IntegrityError as e:

        if type(e.orig) == ForeignKeyViolation:
            return {"msg": f"User with id {data['userId']} not found"}, 404


@jwt_required()
def delete_experience(experience_id):

    experience = EXM.query.get(experience_id)

    if not experience:
        return {"msg": "Experience not found"}, 404

    EXM.query.filter(EXM.id == experience_id).delete()

    current_app.db.session.commit()

    return jsonify({"msg": "Experience deleted"}), 204
