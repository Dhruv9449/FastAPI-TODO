""" Module defining all response and request schemas """

# Import 
from typing import Optional
from datetime import datetime
from pydantic import BaseModel


# Response schemas
class TodoItemResponse(BaseModel):
    """
    Response schema for a todo item.
    """
    id: int


# Request schemas
class TodoItemCreate(BaseModel):
    """
    Request schema for creating a todo item.
    """
    id: int


class TodoItemUpdate(BaseModel):
    """
    Request schema for updating a todo item. Fields that can be updated are title, description and completed.
    """
    id: int


