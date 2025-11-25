from fastapi import FastAPI

from config.database import create_db_and_tables
from routers.user import user_router

app = FastAPI()

create_db_and_tables()

app.include_router(user_router)
