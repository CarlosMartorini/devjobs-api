from app.configs.database import db
from dataclasses import dataclass
import psycopg2
from sqlalchemy.exc import IntegrityError
from flask import current_app

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
    degree = db.Column(db.String(255), nullable=False)
    school = db.Column(db.String(255), nullable=False)
    date_from = db.Column(db.Date())
    date_to = db.Column(db.Date())
    description = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @staticmethod
    def create_one(data):
        new_entry = {
            "user_id" : data["userId"],
            "degree" : data["degree"], 
            "school" : data["school"],
            "date_from" : data["dateFrom"],
            "date_to" : data["dateTo"], 
            "description" : data["description"]
        }

        session = current_app.db.session
        education = EducationModel(**new_entry)

        session.add(education)
        session.commit()


        return {
                "degree" : new_entry["degree"],
                "school" : new_entry["school"],
                "date_from": new_entry["date_from"],
                "date_to": new_entry["date_to"],
                "description" : new_entry["description"]}







