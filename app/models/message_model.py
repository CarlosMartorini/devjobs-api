from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String


@dataclass
class MessageModel(db.Model):

    message: str

    __tablename__ = 'messages'

    message_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    company_id = Column(Integer, ForeignKey('companies.company_id'))
    message = Column(String, nullable=False)
