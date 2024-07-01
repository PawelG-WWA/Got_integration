from flask import Flask
from src.api import setup_blueprints
from src.infrastructure import setup_sqlalchemy, db, setup_sockets
from extensions import setup_extensions
from flask_cors import CORS
import json

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_file("app_config.json", load=json.load)
    app = setup_blueprints(app)
    app = setup_sqlalchemy(app)
    app = setup_extensions(app)
    app = setup_sockets(app)

    return app