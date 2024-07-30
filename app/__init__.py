from flask import Flask

der create_app():
    app = Flask (__name__)
    from .routes import main
    app.register_blueprint(main)
    return app
