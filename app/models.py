""" Module defining all database models"""

# Imports

from sqlalchemy import Column, Integer, String, Boolean 

from app.db import Base


# Table models
class TodoItem(Base):
    """
    TodoItem table model that stores the following data - 
    - id: Unique id for each todo item
    - title: Title of the todo item
    - description: Description of the todo item
    - created_at: Timestamp of when the todo item was created
    - updated_at: Timestamp of when the todo item was last updated
    - completed: Boolean value indicating if the todo item is completed or not
    """
    
    __tablename__ = "todo_items"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(String(255))
    """ 
    created_at: str = Column(DateTime,  default=datetime.now())
    updated_at: str = Column(DateTime,  default=datetime.now())  
    """
    completed = Column(Boolean, default=False)

    """  
        def __init__(self, title, description, completed = False):
        self.id = id
        self.title = title
        self.description = description
        
        self.created_at 
        self.updated_at 
         
        self.completed = completed  
    """
    
    def __repr__(self):
        """
        Function to return the string representation of the TodoItem object.
        Should be of the form <id>. <title>"
        """
        return f'{self.id}. {self.title}'