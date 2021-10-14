from flask import jsonify, request, current_app
from app.models.experience_model import ExperienceModel as EXM
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import NoResultFound

@jwt_required()
def get_experience():

    user_id = int(request.args.get('userId'))

    try:
        experience = EXM.query.filter(EXM.user_id==user_id).all()

    except NoResultFound:
        return {"error" : "User Not in Database" }, 404 
         

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

    experience = EXM.create_one(data)

    if experience == "exeperience exists":

        return {"error" :  "experience already exists"}, 409
    
    return jsonify({"msg" : "created"} ), 201

@jwt_required()
def delete_experience(experience_id):

    experience = EXM.query.get(experience_id)

    if not experience:
        return {"error" : "task not found"}, 404

    EXM.query.filter(EXM.id==experience_id).delete()

    current_app.db.session.commit()

    return jsonify({"msg" : "experience deleted"}), 204
    