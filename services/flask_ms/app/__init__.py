from flask import Flask
from flask_jwt_extended import JWTManager

from config import config
from .models import db


jwt = JWTManager()


def create_app(config_name):
    app = Flask(__name__)
    app.template_folder = '/home/app/web/templates'
    app.config.from_object(config[config_name])

    db.init_app(app)
    jwt.init_app(app)

    from .routes_api import api
    app.register_blueprint(api)
    from .routes_admin import admin
    app.register_blueprint(admin)

    return app