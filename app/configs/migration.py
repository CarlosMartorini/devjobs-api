from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):

    from app.models.user_model import UserModel # noqa : F401
    from app.models.summary_model import SummaryModel  # noqa : F401
    from app.models.education_model import EducationModel  # noqa : F401
    from app.models.experience_model import ExperienceModel  # noqa : F401
    from app.models.company_model import CompanyModel  # noqa : F401
    from app.models.tech_skill_model import TechSkillModel # noqa : F401
    from app.models.other_skill_model import OtherSkillModel # noqa : F401

    Migrate(app, app.db)
