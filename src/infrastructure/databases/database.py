from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()


def setup_sqlalchemy(app):
    db.init_app(app)
    return app