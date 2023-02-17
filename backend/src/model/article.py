
from datetime import datetime as dt

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.mysql import LONGTEXT

from . import Base


class Article(Base):
  """Article profile"""

  __tablename__ = "article"

  id = Column(Integer, primary_key=True)
  title = Column(String(200), nullable=True)
  content = Column(LONGTEXT, nullable=True)
  created_on = Column(DateTime, default=dt.utcnow)
  last_updated = Column(DateTime, default=dt.utcnow)
  
  def __repr__(self) -> str:
    return f"Article {self.id}: {self.title}. Created on {self.created_on}"