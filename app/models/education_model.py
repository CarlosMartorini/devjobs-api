from app.configs.database import db
from dataclasses import dataclass
from flask import current_app


@dataclass
class EducationModel(db.Model):

    id: int
    user_id: int
    degree: str
    school: str
    dateFrom: str
    dateTo: str
    description: str

    __tablename__ = "education"

    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(255), nullable=False)
    school = db.Column(db.String(255), nullable=False)
    dateFrom = db.Column(db.Date())
    dateTo = db.Column(db.Date())
    description = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @staticmethod
    def create_one(data):

        new_entry = {
            "user_id": data["userId"],
            "degree": data["degree"],
            "school": data["school"],
            "date_from": data["dateFrom"],
            "date_to": data["dateTo"],
            "description": data["description"]
        }

        session = current_app.db.session
        education = EducationModel(**new_entry)

        session.add(education)
        session.commit()

        return {
                "degree": new_entry["degree"],
                "school": new_entry["school"],
                "date_from": new_entry["dateFrom"],
                "date_to": new_entry["dateTo"],
                "description": new_entry["description"]}
