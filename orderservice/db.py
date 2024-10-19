from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from orderservice import setting
from sqlmodel import SQLModel, Session, create_engine


connection_string = str(setting.DATABASE_URL).replace(
    "postgresql" , "postgresql+psycopg"
)

engine = create_engine(connection_string)

def create_db_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app:FastAPI)->AsyncGenerator[None,None]:
    print("creating tables for orderService")
    create_db_tables()
    yield

def get_session():
    with Session(engine) as session:
        yield session
