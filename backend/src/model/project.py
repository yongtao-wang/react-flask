from datetime import datetime as dt

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import LONGTEXT

from database import Base


class Project(Base):
    """Project profile"""

    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    description = Column(LONGTEXT, nullable=True)

    created_on = Column(DateTime, default=dt.utcnow)
    updated_on = Column(DateTime, default=dt.utcnow)

    created_by = Column(String(128), ForeignKey('user.id'), nullable=True)

    def __repr__(self) -> str:
        return f"Project {self.id}: {self.name}. Created on {self.created_on} by {self.created_by}"
