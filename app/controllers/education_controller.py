from flask import jsonify, request, current_app
from app.models.education_model import EducationModel as EM
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import NoResultFound


@jwt_required()
def get_education():

    user_id = int(request.args.get('userId'))

    try:
        education = EM.query.filter(EM.user_id == user_id).all()

    except NoResultFound:
        return {"error": "User Not in Database"}, 404

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

    EM.create_one(data)

    return jsonify({"msg": "created"}), 201


@jwt_required()
def delete_education(education_id):

    education = EM.query.get(education_id)

    if not education:
        return {"error": "task not found"}, 404

    EM.query.filter(EM.id == education_id).delete()

    current_app.db.session.commit()

    return jsonify({"msg": "education deleted"}), 204
