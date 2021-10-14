from flask import Blueprint
from app.controllers.summary_controller import create_summary, update_summary, get_summary


bp = Blueprint('summary_bp', __name__, url_prefix='/summary')


bp.post('')(create_summary)
bp.patch('')(update_summary)
bp.get('')(get_summary)
