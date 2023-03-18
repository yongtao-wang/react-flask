from datetime import datetime as dt

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.mysql import LONGTEXT

from database import Base


class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(LONGTEXT, nullable=True)
    created_on = Column(DateTime, default=dt.utcnow)
    last_updated = Column(DateTime, default=dt.utcnow)

    def __init__(self, title, content=None, created_on=None, last_updated=None):
        self.title = title
        self.content = content
        self.created_on = created_on
        self.last_updated = last_updated

    def __repr__(self):
        return f'Article {self.id}: {self.title}, created on {self.created_on}'
