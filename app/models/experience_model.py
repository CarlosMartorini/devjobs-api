
from app.configs.database import db
from dataclasses import dataclass
from flask import current_app


@dataclass
class ExperienceModel(db.Model):

    id: int
    user_id: int
    role: str
    company: str
    dateFrom: str
    dateTo: str
    description: str

    __tablename__ = "experiences"

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(255), nullable=False)
    dateFrom = db.Column(db.Date())
    dateTo = db.Column(db.Date())
    description = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @staticmethod
    def create_one(data):
        new_entry = {
            "user_id": data["userId"],
            "role": data["role"],
            "company": data["company"],
            "date_from": data["dateFrom"],
            "date_to": data["dateTo"],
            "description": data["description"]
        }

        session = current_app.db.session
        experience = ExperienceModel(**new_entry)

        session.add(experience)
        session.commit()

        return {
                "role": new_entry["role"],
                "company": new_entry["company"],
                "date_from": new_entry["dateFrom"],
                "date_to": new_entry["dateTo"],
                "description": new_entry["description"]
                }
