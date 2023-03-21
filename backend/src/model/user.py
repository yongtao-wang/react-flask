from datetime import datetime as dt

from marshmallow import Schema, fields
from sqlalchemy import Boolean, Column, DateTime, Integer, String, UnicodeText

from database import Base


class User(Base):
    """User profile"""

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(UnicodeText(128), nullable=False)
    first_name = Column(UnicodeText(100))
    last_name = Column(UnicodeText(100))
    title = Column(UnicodeText(100))
    email = Column(String(100))

    last_updated = Column(DateTime, default=dt.utcnow)
    is_deleted = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f'User {self.name}, id: {self.id}, title: {self.title}, deleted: {self.deleted}'


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    title = fields.Str()
    email = fields.Str()
    last_updated = fields.DateTime()
    is_deleted = fields.Boolean()
