from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, Text


@dataclass
class MessageModel(db.Model):

    message: str
    id: int
    companyId: int
    userId: int

    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('users.id'), nullable=False)
    companyId = Column(Integer, ForeignKey('companies.id'), nullable=False)
    message = Column(Text, nullable=False)
