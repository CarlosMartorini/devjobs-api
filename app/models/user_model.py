from app.configs.database import db
from dataclasses import dataclass


@dataclass
class UserModel(db.Model):

    id: int
    email: str
    password: str
    first_name: str
    last_name: str
    birth_date: str
    linkedin_profile: str
    address: str
    phone: str

    __tabelname__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(127), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.Date(), nullable=False)
    linkedin_profile = db.Column(db.String(127), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
