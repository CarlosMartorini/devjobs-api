from flask import current_app, request, jsonify
from flask_jwt_extended.utils import create_access_token

from app.models.company_model import CompanyModel

from sqlalchemy.exc import IntegrityError, NoResultFound
from psycopg2.errors import UniqueViolation
from app.exc.company_exc import InvalidPasswordError


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


def login():
    try:

        data = request.get_json()

        company: CompanyModel = CompanyModel.query.filter_by(email=data['email']).one()

        company.verify_password(data['password'])

        return {"access_token": create_access_token(company)}

    except InvalidPasswordError as e:
        return {"msg": e.message}, 401

    except KeyError as e:
        key = e.args[0].split(' ')[0]
        return {'msg': f'key {key} is not found'}, 400

    except NoResultFound:
        return {'msg': f'User with email {data["email"]} is not found'}, 404
