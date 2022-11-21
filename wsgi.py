import os

from sqla_encrypt_poc.entrypoints.flask_app import create_app

app = create_app(os.environ.get("FLASK_CONFIG", "default"))
