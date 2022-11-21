from flask import Blueprint

api = Blueprint("api", __name__)

# circular import 방지
from sqla_encrypt_poc.entrypoints.flask_app.api.identity import *
