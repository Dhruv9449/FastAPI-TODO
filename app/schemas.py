""" Module defining all response and request schemas """

# Import 
from typing import Optional
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
    id: Optional[int]
    title: str
    description: str
    """  
    created_at: Optional[datetime]
    updated_at: Optional[datetime] 
    """
    completed: Optional[bool] = False
    

class TodoItemUpdate(BaseModel):
    """
    Request schema for updating a todo item. Fields that can be updated are title, description and completed.
    """
    id: int


