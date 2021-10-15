from flask import jsonify, request, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.message_model import MessageModel


@jwt_required()
def create_message():
    data = request.get_json()
    message = MessageModel(**data)

    session = current_app.db.session
    session.add(message)
    session.commit()

    return jsonify(message), 201


@jwt_required()
def get_user_messages():
    user_id = get_jwt_identity()['id']

    messages = MessageModel.query.filter_by(user_id=user_id).all()

    # Adicionar o nome da empresa e o nome do dev

    return jsonify(messages)


@jwt_required()
def get_company_messages():
    company_id = get_jwt_identity()['company_id']

    # Adicionar o nome da empresa e o nome do dev

    messages = MessageModel.query.filter_by(company_id=company_id).all()
    return jsonify(messages)
