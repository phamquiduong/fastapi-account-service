from pydantic import EmailStr
from sqlmodel import SQLModel


class UserUpdateSchema(SQLModel):
    username: str
    email: EmailStr | None
