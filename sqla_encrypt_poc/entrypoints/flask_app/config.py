import os

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_USER = os.environ.get("DB_USER", "oidc")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "secret11!")
DB_DATABASE = os.environ.get("DB_DATABASE", "oidc")
DB_ENGINE = os.environ.get("DB_ENGINE", "postgres")
DB_SCHEME = "postgresql+psycopg2"

SQLALCHEMY_DATABASE_URI = (
    f"{DB_SCHEME}://"
    f"{DB_USER}:{DB_PASSWORD}@"
    f"{DB_HOST}:{DB_PORT}/"
    f"{DB_DATABASE}"
)


class Config:
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig
}
