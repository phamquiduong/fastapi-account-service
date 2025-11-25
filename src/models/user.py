from models.base import BaseModel


class UserModel(BaseModel, table=True):
    __tablename__: str = 'users'

    username: str
    password: str
