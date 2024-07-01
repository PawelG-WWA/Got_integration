from .contact import contact_blueprint

def setup_blueprints(app):
    app.register_blueprint(contact_blueprint)
    return app


__all__ = ['setup_blueprints']