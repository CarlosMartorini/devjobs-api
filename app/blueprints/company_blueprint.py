from flask import Blueprint
from app.controllers.company_controller import create_company, login


company_bp = Blueprint('company_bp', __name__, url_prefix='companies')

company_bp.post('')(create_company)
company_bp.post('/login')(login)