from flask import Blueprint
from app.controllers.experience_controller import get_experience, create_experience, delete_experience

bp = Blueprint('experience_bp', __name__, url_prefix='/experience')

bp.get('')(get_experience)
bp.post('')(create_experience)
bp.delete('/<experience_id>')(delete_experience)
