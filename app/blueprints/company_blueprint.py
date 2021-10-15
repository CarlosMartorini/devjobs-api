from flask import Blueprint
from app.controllers.company_controller import create_company, login


bp = Blueprint('company_bp', __name__, url_prefix='companies')

bp.post('')(create_company)
bp.post('/login')(login)
