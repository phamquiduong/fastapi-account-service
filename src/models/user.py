from sqlmodel import Field

from models.base import BaseModel


class UserModel(BaseModel, table=True):
    __tablename__: str = 'users'

    username: str = Field(unique=True, index=True)
    password: str = Field(exclude=True)
