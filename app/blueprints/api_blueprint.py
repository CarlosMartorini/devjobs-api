from flask import Blueprint
from .message_blueprint import message_bp


api_bp = Blueprint('api_bp', __name__, url_prefix='/api')

api_bp.register_blueprint(message_bp)
