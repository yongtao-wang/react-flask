import logging

from flask import Flask, jsonify, render_template
from flask_cors import CORS
from sqlalchemy import create_engine

from controller.users import users
import cfg


config = cfg.init()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)  # load config
    app.logger.setLevel(logging.INFO)

    headers = ['accept', 'origin', 'Content-Type']
    origins = ['http://localhost:4200/*', 'http://localhost:5000/*']
    CORS(app, origins=origins, allow_headers=headers, supports_credentials=True)

    register_blueprints(app)
    register_error_handler(app)
    register_cli(app)
    return app


def register_blueprints(app: Flask):
    """Register Flask blueprints"""
    app.register_blueprint(users)


def register_cli(app: Flask):
    """Register Click commands"""
    pass


def register_error_handler(app: Flask):
    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({'data': "Page not found"}, 404)

    @app.errorhandler(401)
    def user_unauthorized(e):
        return "401", 401


db = create_engine(config.DATABASE_URI)
app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
