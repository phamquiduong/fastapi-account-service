from sqlalchemy import create_engine
from sqlmodel import SQLModel

SQLITE_FILE_NAME = '../db.sqlite3'
SQLITE_URL = f'sqlite:///{SQLITE_FILE_NAME}'

connect_args = {'check_same_thread': False}
engine = create_engine(SQLITE_URL, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
