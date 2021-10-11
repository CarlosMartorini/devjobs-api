from flask import request, jsonify, current_app
from app.models.summary_model import SummaryModel


def create_summary():
    session = current_app.db.session

    data = request.get_json()

    new_summary = SummaryModel(**data)

    # TODO: user_id

    session.add(new_summary)
    session.commit()

    return jsonify(new_summary), 201


def update_summary():
    ...


def get_summary(id: int):
    ...


def delete_summary():
    ...
