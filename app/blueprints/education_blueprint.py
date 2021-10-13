from flask import Blueprint
from app.controllers.education_controller import get_education, create_education, delete_education


bp = Blueprint('user_bp', __name__, url_prefix='/education')


api_bp.get('/')(get_education)
api_bp.post('/<id>')(create_education)
api_bp.delete('/<id>')(delete_education)
