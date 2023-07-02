from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.repository.database import Base


class TodoItemModel(Base):

    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    # title = Column(String, max_length=100)
    title = Column(String(100))
    # description = Column(String, max_length=1000)
    description = Column(String(1000))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    status = Column(String)
