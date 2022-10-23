# Imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import models, routers
from app.db import engine
from app.config import settings


# Creating all database models
models.Base.metadata.create_all(bind=engine)


# Creating FastAPI app instance
app = FastAPI()


# Allowed origins for CORS
origins = [] + settings.cors_origin_whitelist


# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Root route
@app.get("/")
async def root():
    """ Root route """
    return {"message": "Welcome to TODO API! Head over to - https://github.com/Dhruv9449/FastAPI-TODO for more info."}

app.include_router(routers.router)