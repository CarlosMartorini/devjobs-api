from flask import jsonify, request, current_app
from flask_jwt_extended import jwt_required
from app.configs.database import db

from app.models.message_model import MessageModel
from app.models.company_model import CompanyModel

from psycopg2.errors import NotNullViolation
from sqlalchemy.exc import IntegrityError


VALID_KEYS = ['userId', 'companyId', 'message']


@jwt_required()
def create_message():
    try:
        data = request.get_json()
        message = MessageModel(**data)

        session = current_app.db.session
        session.add(message)
        session.commit()

        return jsonify(message), 201

    except TypeError as e:
        invalid_key = e.args[0].split(' ')[0].strip("'")

        return {
            'invalid_keys': invalid_key,
            'Keys': VALID_KEYS
        }, 400

    except IntegrityError as e:

        if type(e.orig) == NotNullViolation:
            doble_quote = '"'
            single_quote = "'"
            invalid_key = e.args[0].split(' ')[5].replace(doble_quote, single_quote)
            return {'msg': f'Key {invalid_key} not found'}, 400


@jwt_required()
def get_user_messages():
    userId = request.args.get('userId')

    if not userId:
        return {"msg": "Argument userId is required"}, 400

    messages = db.session.query(MessageModel, CompanyModel).select_from(MessageModel).join(CompanyModel).filter(MessageModel.userId == int(userId)).all() # noqa

    list_messages = [{
        "message": message[0].message,
        "companyName": message[1].companyName,
        "userId": message[0].user_id,
        "CompanyId": message[0].company_id
    } for message in messages]

    return jsonify(list_messages), 200


@jwt_required()
def delete_message(message_id):

    mess_id = int(message_id)

    message = MessageModel.query.get(mess_id)

    if not message:
        return {"msg": "Message not found"}, 404

    MessageModel.query.filter_by(id=message_id).delete()

    current_app.db.session.commit()

    return 'Deleted', 204
