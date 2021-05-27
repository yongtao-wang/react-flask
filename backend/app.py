import logging

from flask import Flask, render_template
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config = {}  # a cfg2 similarity
    app.logger.setLevel(logging.INFO)

    headers = ['accept', 'origin', 'Content-Type']
    origins = ['http://localhost:4200/*', 'http://localhost:5000/*']
    CORS(app, origins=origins, allow_headers=headers, supports_credentials=True)

    configure_extensions(app)
    register_blueprints(app)


def configure_extensions(app):
    # load config
    db_conn_uri = 'mysql+pymysql://{username}:{password}@{host}/{db}'


def register_blueprints(app):
    """Register Flask blueprints"""
    pass
