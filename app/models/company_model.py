from app.configs.database import db

from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash

from app.exc.company_exc import InvalidPasswordError



@dataclass
class CompanyModel(db.Model):
    id: int
    email: str
    companyName: str

    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(127), nullable=False)
    companyName = db.Column(db.String(255), nullable=False)


    # users = db.relationship("MessageModel", backref=db.backref('user'))
    
    @property
    def password(self):
        raise AttributeError('Password cannot be accessed')

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, request_password):
        is_correct_password = check_password_hash(self.password_hash, request_password)
        if not is_correct_password:
            raise InvalidPasswordError()
