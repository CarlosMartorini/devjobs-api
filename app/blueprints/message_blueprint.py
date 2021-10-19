from flask import Blueprint

from app.controllers.message_controller import (
    create_message,
    # get_company_messages,
    get_user_messages,
    # get_all_messages,
    delete_message

    )

bp = Blueprint('message_bp', __name__, url_prefix='messages')

bp.post('')(create_message)
# bp.get('')(get_all_messages)
# bp.get('/company')(get_company_messages)
bp.get('')(get_user_messages)
bp.delete('/<message_id>')(delete_message)
