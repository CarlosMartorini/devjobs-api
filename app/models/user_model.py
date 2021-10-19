from app.configs.database import db
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash



@dataclass
class UserModel(db.Model):

    id: int
    email: str
    firstName: str
    lastName: str
    birthDate: str
    linkedinProfile: str
    address: str
    phone: str

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(127), nullable=False)
    firstName = db.Column(db.String(255), nullable=False)
    lastName = db.Column(db.String(255), nullable=False)
    birthDate = db.Column(db.Date(), nullable=False)
    linkedinProfile = db.Column(db.String(127), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)

    # companies = db.relationship("MessageModel", back_populates="user")

    companies = db.relationship("MessageModel", backref=db.backref('company'))
    


    

    @property
    def password(self):
        raise AttributeError('Password cannot be accessed!')

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
