from app import db_engine


def init():
    db_engine.create_all()