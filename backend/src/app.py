import logging

from flask import Flask, render_template
from flask_cors import CORS
from sqlalchemy import create_engine

from . import cfg


config = cfg.init()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)  # load config
    app.logger.setLevel(logging.INFO)

    headers = ['accept', 'origin', 'Content-Type']
    origins = ['http://localhost:4200/*', 'http://localhost:5000/*']
    CORS(app, origins=origins, allow_headers=headers, supports_credentials=True)

    register_blueprints(app)
    register_cli(app)


def register_blueprints(app):
    """Register Flask blueprints"""
    pass


def register_cli(app):
    """Register Click commands"""
    pass


db_engine = create_engine(config.DATABASE_URI)
app = create_app()
