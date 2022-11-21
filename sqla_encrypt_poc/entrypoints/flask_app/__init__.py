from flask import Flask

from sqla_encrypt_poc.entrypoints.flask_app.api import api as api_bp
from sqla_encrypt_poc.entrypoints.flask_app.config import config
from sqla_encrypt_poc.entrypoints.flask_app.database import db, migrate


def create_app(config_name="default"):
    app = Flask(__name__)
    app_config = config[config_name]
    app.config.from_object(app_config)
    app_config.init_app(app)

    app.register_blueprint(api_bp, url_prefix="/api")

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def index():
        return "hello world"

    return app
