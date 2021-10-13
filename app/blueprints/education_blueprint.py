from flask import Blueprint
from app.controllers.education_controller import get_education, create_education, delete_education

bp = Blueprint('education_bp', __name__, url_prefix='/education')

bp.get('')(get_education)
bp.post('')(create_education)
bp.delete('/<education_id>')(delete_education)
