from flask import Blueprint

from app.controllers.message_controller import create_message, get_company_messages, get_user_messages

message_bp = Blueprint('message_bp', __name__, url_prefix='messages')

message_bp.post('')(create_message)
message_bp.get('/company')(get_company_messages)
message_bp.get('/user')(get_user_messages)
