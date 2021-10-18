from app.configs.database import db
from dataclasses import dataclass


@dataclass
class OtherSkillModel(db.Model):
    id: int
    user_id: int
    description: str
    level: str

    __tablename__ = "others_skills"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    level = db.Column(db.String(255), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
