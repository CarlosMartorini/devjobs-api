from flask import current_app, request, jsonify
from app.models.company_model import CompanyModel
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError


VALID_KEYS = ['email', 'company_name', 'password']


def create_company():
    try:
        data = request.get_json()

        password_to_hash = data.pop('password')

        company = CompanyModel(**data)
        company.password = password_to_hash

        session = current_app.db.session

        session.add(company)
        session.commit()

        return jsonify(company), 201

    except IntegrityError as e:

        if type(e.orig) == UniqueViolation:
            return {'msg': 'Email already exists!'}, 409

    except TypeError as e:
        single_quote = "'"
        invalid_key = e.args[0].split(' ')[0].strip(single_quote)

        return {
            'invalid_key': invalid_key,
            'valid_keys': VALID_KEYS
        }, 400
