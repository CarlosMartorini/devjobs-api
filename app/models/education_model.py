from app.configs.database import db
from dataclasses import dataclass


@dataclass
class EducationModel(db.Model):

    id: int
    user_id: int
    degree: str
    school: str
    date_from: str
    date_to: str
    description: str

    __tablename__ = "education"


    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    degree = db.Column(db.String(255), nullable=False)
    school = db.Column(db.String(255), nullable=False)
    date_from = db.Column(db.String(255), nullable=False)
    date_to = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(511), nullable=False)
