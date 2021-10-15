from flask import Blueprint
from app.controllers.tech_skill_controller import create_skill, get_skills_by_userId, get_users_by_one_skill, update_skill, delete_skill

bp = Blueprint('tech_skills_bp', __name__, url_prefix='/techskills')

bp.post("")(create_skill)
bp.get('')(get_skills_by_userId)
bp.get('/<description_like>/<level_like>')(get_users_by_one_skill)
bp.patch('/<skill_id>')(update_skill)
bp.delete('/<skill_id>')(delete_skill)