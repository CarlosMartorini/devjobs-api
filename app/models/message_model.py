from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, Text


@dataclass
class MessageModel(db.Model):

    message: str
    id: int
    company_id: int
    user_id: int

    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))
    message = Column(Text, nullable=False)
    