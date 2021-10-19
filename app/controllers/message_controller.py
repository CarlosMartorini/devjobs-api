from flask import jsonify, request, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.configs.database import db

from app.models.message_model import MessageModel
from app.models.company_model import CompanyModel


# @jwt_required()
def create_message():
    data = request.get_json()
    message = MessageModel(**data)

    session = current_app.db.session
    session.add(message)
    session.commit()

    return jsonify(message), 201


# @jwt_required()
def get_user_messages():
    user_id = int(request.args.get('userId'))

    messages = db.session.query(MessageModel, CompanyModel).select_from(MessageModel).join(CompanyModel).filter(MessageModel.user_id == user_id).all()

    list_messages = [{
        "message" : message[0].message,
        "companyName" : message[1].company_name,
        "userId" : message[0].user_id,
        "CompanyId" : message[0].company_id
    } for message in messages]

    return jsonify(list_messages),200


# @jwt_required()
def delete_message(message_id):

    mess_id= int(message_id)

    message = MessageModel.query.get(mess_id)  

    if not message:
        return {"error" : "Message not found"}, 404
    
    MessageModel.query.filter_by(id=message_id).delete()

    current_app.db.session.commit()

    return 'Deleted', 204
