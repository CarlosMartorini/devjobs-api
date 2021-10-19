from flask import jsonify, request, current_app
from app.models.education_model import EducationModel as EM
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import NoResultFound, IntegrityError
from psycopg2.errors import ForeignKeyViolation


VALID_KEYS = [
    "user_id",
    "degree",
    "school",
    "dateFrom",
    "dateTo",
    "description"
]


@jwt_required()
def get_education():

    try:
        user_id = int(request.args.get('userId'))

        education = EM.query.filter(EM.user_id == user_id).all()

    except NoResultFound:
        return {"msg": "User Not in Database"}, 404

    except TypeError:
        return {"msg": "Argument userId not found"}, 400

    return jsonify(education), 200


@jwt_required()
def create_education():

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
        output = EM.create_one(data)

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
def delete_education(education_id):

    education = EM.query.get(education_id)

    if not education:
        return {"msg": "Education not found"}, 404

    EM.query.filter(EM.id == education_id).delete()

    current_app.db.session.commit()

    return jsonify({"msg": "education deleted"}), 204
