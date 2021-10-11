from flask import Blueprint
from . import user_blueprint

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')

api_bp.register_blueprint(user_blueprint.bp)
