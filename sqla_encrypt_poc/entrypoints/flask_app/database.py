from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from sqla_encrypt_poc.repository.sqla.base import Base

db = SQLAlchemy(model_class=Base)
migrate = Migrate()
