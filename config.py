import os

base_dir = os.path.dirname(os.path.abspath(__file__))


class BaseConfig:
    """Base configuration"""

    APP_NAME = os.getenv("APP_NAME", "Flask app")
    SECRET_KEY = os.getenv("SECRET_KEY", "Ensure you set a secret key!")
    DEBUG_TB_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False

    @staticmethod
    def configure(app):
        pass


class MailConfig:
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False

class DevelopmentConfig(BaseConfig, MailConfig):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEVELOPMENT_DATABASE_URL", "sqlite:///" + os.path.join(base_dir, "development.sqlite3"),)


class ProductionConfig(BaseConfig, MailConfig):

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///" + os.path.join(base_dir, "production.sqlite3"))
    WTF_CSRF_ENABLED = True

config = dict(development=DevelopmentConfig, production=ProductionConfig)