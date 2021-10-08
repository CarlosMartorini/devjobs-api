from flask import Blueprint
from app.controllers.user_controller import create_user, get_user


bp = Blueprint('user_bp', __name__, url_prefix='/users')


bp.post('')(create_user)
bp.get('/<int:id>')(get_user)
