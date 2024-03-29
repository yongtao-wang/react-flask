import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import cfg


config = cfg.init()
Logger = logging.getLogger(__name__)

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Session = scoped_session(sessionmaker(autoflush=False, bind=engine))
Base = declarative_base()
Base.query = Session.query_property()


def init_db():
    from model.article import Article
    Base.metadata.create_all(bind=engine)
    Logger.info('Database Initiated.')

