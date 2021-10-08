from flask import Blueprint

from app.controllers.education_controller import(
    create_education,
    delete_education,
    get_education
)

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')


api_bp.get('/education')(get_education)
api_bp.post('/education/<id>')(create_education)
api_bp.delete('/signin/<id>')(delete_education)
