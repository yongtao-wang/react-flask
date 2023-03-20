from datetime import datetime as dt

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
        return f"User {self.name}, id: {self.id}, title: {self.title}, deleted: {self.deleted}"
