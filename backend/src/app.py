import logging

from flask import Flask, jsonify
from flask_cors import CORS

from controller.articles import articles
from database import init_db, Session
import cfg

config = cfg.init()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.logger.setLevel(logging.INFO)

    headers = ['accept', 'origin', 'Content-Type']
    origins = ['http://localhost:4200/*', 'http://localhost:5000/*', 'http://localhost:3000/*']
    CORS(app, origins=origins, allow_headers=headers, supports_credentials=True)

    register_blueprints(app)
    register_cli(app)
    register_error_handlers(app)

    init_db()
    return app


def register_blueprints(app: Flask):
    """Register Flask Blueprints"""
    app.register_blueprint(articles)
    pass


def register_cli(app: Flask):
    """Register Click Commands"""
    pass


def register_error_handlers(app: Flask):
    @app.errorhandler(404)
    def page_not_found(e):
        # TODO: return render_template('404.html'), 404
        return "Page Not Found - 404", 404

    @app.errorhandler(401)
    def user_unauthorized(e):
        # TODO: return render_template('401.html'), 401
        return "Unauthorized - 401", 401


app = create_app()


@app.teardown_appcontext
def shutdown_db_session(exception=None):
    Session.remove()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4200)
