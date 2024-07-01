from flask_migrate import Migrate
from src.infrastructure import db
import src.core.domain.models


migrate = Migrate()


def setup_extensions(app):
    migrate.init_app(app, db)
    return app
    