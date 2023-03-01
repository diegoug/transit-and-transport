from os import environ, path
basedir = path.abspath(path.dirname(__file__))


class Config:
    DEBUG = False
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "new_secret_key_:D"

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')

config = {
    'development': "config.development.DevelopmentConfig",
    'production': ProductionConfig,
    'default': "config.development.DevelopmentConfig",
}
