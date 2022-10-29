""" Module defining all database models"""

# Imports
from xmlrpc.client import Boolean
from sqlalchemy import Column, Integer, String, TIMESTAMP 

from app.db import Base


# Table models
class TodoItem(Base):
    __tablename__ = "todo_items"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String(length = 300))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    completed = Column(Boolean)

    def __repr__(self):
        """
        Function to return the string representation of the TodoItem object.
        Should be of the form <id>. <title>"
        """
        pass