from flask import Blueprint

from app.controllers.message_controller import create_message, get_company_messages, get_user_messages

bp = Blueprint('message_bp', __name__, url_prefix='messages')

bp.post('')(create_message)
bp.get('/company')(get_company_messages)
bp.get('/user')(get_user_messages)
