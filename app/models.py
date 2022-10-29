""" Module defining all database models"""

# Imports
from email.policy import default
from enum import unique
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, func

from app.db import Base


# Table models
class TodoItem(Base):
    __tablename__ = "todo_items"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=False)
    description = Column(String(length = 300), unique=False)
    created_at = Column(TIMESTAMP, default = func.now())
    updated_at = Column(TIMESTAMP, default = func.now())
    completed = Column(Boolean, unique= False)

    def __repr__(self):
        return f'id={self.id} title={self.title}'