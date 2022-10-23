""" Module handling routes for the application """

# Imports
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.db import get_db


# Creating FastAPI router
router = APIRouter(tags=["Todo Items"])

# Routes

@router.get("/todo-items/", response_model=List[schemas.TodoItemResponse])
async def get_todo_items(db: Session = Depends(get_db)):
    """
    Route to get all todo items from the database sorted in descending order of creation.
    """
    pass


@router.get("/todo-items/{todo_item_id}", response_model=schemas.TodoItemResponse)
async def get_todo_item(todo_item_id: int, db: Session = Depends(get_db)):
    """
    Route to get a specific todo item from the database.
    """
    pass


@router.post("/todo-items/", response_model=schemas.TodoItemResponse, status_code=status.HTTP_201_CREATED)
async def create_todo_item(todo_item: schemas.TodoItemCreate, db: Session = Depends(get_db)):
    """
    Route to create a new todo item in the database.
    """
    pass


@router.put("/todo-items/{todo_item_id}", response_model=schemas.TodoItemResponse)
async def update_todo_item(todo_item_id: int, todo_item: schemas.TodoItemUpdate, db: Session = Depends(get_db)):
    """
    Route to update a specific todo item in the database.
    """
    pass


@router.delete("/todo-items/{todo_item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo_item(todo_item_id: int, db: Session = Depends(get_db)):
    """
    Route to delete a specific todo item from the database.
    """
    pass
