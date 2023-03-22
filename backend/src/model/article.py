from datetime import datetime as dt

from marshmallow import Schema, fields
from sqlalchemy import Boolean, Column, Integer, String, DateTime, UnicodeText
from sqlalchemy.dialects.mysql import LONGTEXT

from database import Base


class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    author = Column(UnicodeText, nullable=True)
    content = Column(LONGTEXT, nullable=True)
    created_on = Column(DateTime, default=dt.utcnow)
    last_updated = Column(DateTime, default=dt.utcnow)
    is_deleted = Column(Boolean, default=False)
    is_hidden = Column(Boolean, default=False)

    def __repr__(self):
        return f'Article {self.id}: {self.title}, created on {self.created_on}'


class ArticleSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    author = fields.Str()
    content = fields.Str()
    created_on = fields.DateTime()
    last_updated = fields.DateTime()
    is_deleted = fields.Bool()
    is_hidden = fields.Bool()
