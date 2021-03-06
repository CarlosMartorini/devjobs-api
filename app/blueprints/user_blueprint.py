from flask import Blueprint
from app.controllers.user_controller import create_user, get_relationships_user, login, get_user


bp = Blueprint('user_bp', __name__, url_prefix='/users')


bp.post('')(create_user)
bp.post('/login')(login)
bp.get('/<int:id>')(get_user)
bp.get('/<int:id>/relationships')(get_relationships_user)
