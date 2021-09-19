from datetime import datetime as dt

from sqlalchemy import Boolean, Column, DateTime, Integer, String, UnicodeText

from . import Base


class User(Base):
    """User profile"""

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(UnicodeText(128), nullable=False)
    first_name = Column(UnicodeText(100))
    last_name = Column(UnicodeText(100))
    title = Column(UnicodeText(100))
    email = Column(String(100))

    updated = Column(DateTime, default=dt.utcnow)
    deleted = Column(Boolean, default=False)
