from flask import Blueprint
from .company_blueprint import company_bp

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')

api_bp.register_blueprint(company_bp)
