from app.configs.database import db
from dataclasses import dataclass


@dataclass
class SummaryModel(db.Model):

    id: int
    objective: str
    city: str
    speciality: str
    disponibility: str
    experienceTime: int
    user_id: int

    __tablename__ = "summaries"

    id = db.Column(db.Integer, primary_key=True)
    objective = db.Column(db.String(1023), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    speciality = db.Column(db.String(255), nullable=False)
    disponibility = db.Column(db.String(255), nullable=False)
    experienceTime = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
