from flask import Blueprint
from . import (
    user_blueprint,
    education_blueprint,
    experience_blueprint,
    summary_blueprint,
    company_blueprint,
<<<<<<< HEAD
    tech_skills_blueprint,
    other_skill_blueprint
=======
    message_blueprint
>>>>>>> 38260bf8547b9bad12f2ef3a841aa792d519f592
)


api_bp = Blueprint('api_bp', __name__, url_prefix='/api')


api_bp.register_blueprint(user_blueprint.bp)
api_bp.register_blueprint(tech_skills_blueprint.bp)
api_bp.register_blueprint(other_skill_blueprint.bp)
api_bp.register_blueprint(education_blueprint.bp)
api_bp.register_blueprint(experience_blueprint.bp)
api_bp.register_blueprint(summary_blueprint.bp)
api_bp.register_blueprint(company_blueprint.bp)
api_bp.register_blueprint(message_blueprint.bp)
