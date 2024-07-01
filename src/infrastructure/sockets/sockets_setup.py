from flask_socketio import SocketIO


socketio = SocketIO()


def setup_sockets(app):
    socketio.init_app(app, cors_allowed_origins="*", logger=True, engineio_logger=True)
    from .setup_handlers import setup_socketio_handlers
    setup_socketio_handlers()
    return app