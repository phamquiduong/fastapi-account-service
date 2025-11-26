from typing import Annotated

from fastapi import HTTPException, status
from fastapi.params import Depends

from dependencies.password import PasswordServiceDep
from dependencies.session import SessionDep
from models.user import UserModel
from services.user import UserService


async def get_user_service(session: SessionDep, password_service: PasswordServiceDep):
    yield UserService(session=session, password_service=password_service)

UserServiceDep = Annotated[UserService, Depends(get_user_service)]


async def get_user_from_path(user_service: UserServiceDep, user_id: str) -> UserModel:
    user = user_service.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

UserFromPathDep = Annotated[UserModel, Depends(get_user_from_path)]
