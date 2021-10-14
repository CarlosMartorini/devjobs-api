from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):

    from app.models.user_model import UserModel
    from app.models.summary_model import SummaryModel

    Migrate(app, app.db)
