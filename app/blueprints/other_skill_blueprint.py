from flask import Blueprint
from app.controllers.other_skill_controller import create_other_skill, get_others_skills_by_user, get_by_other_skill, update_other_skill, delete_other_skill

bp = Blueprint('others_skills_bp', __name__, url_prefix='/otherskills')

bp.post("")(create_other_skill)
bp.get('')(get_others_skills_by_user)
bp.get('/<description_like>/<level_like>')(get_by_other_skill)
bp.patch('/<skill_id>')(update_other_skill)
bp.delete('/<skill_id>')(delete_other_skill)
