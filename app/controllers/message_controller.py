from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.message_model import MessageModel


@jwt_required()
def create_message():
    data = request.get_json()
    message = MessageModel(**data)

    return jsonify(message), 201


@jwt_required()
def get_user_messages():
    user_id = get_jwt_identity()['user_id']

    messages = MessageModel.query.filter_by(user_id=user_id).all()

    return jsonify(messages)


@jwt_required()
def get_company_messages():
    company_id = get_jwt_identity()['company_id']

    messages = MessageModel.query.filter_by(company_id=company_id).all()
    return jsonify(messages)
