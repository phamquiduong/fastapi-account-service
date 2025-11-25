import uuid

from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    id: uuid.UUID
    username: str
    password: str = Field(exclude=True)
