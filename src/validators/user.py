from fastapi import HTTPException, status

from dependencies.user import UserServiceDep
from models.user import UserModel
from schemas.user.create import UserCreateSchema
from schemas.user.update import UserUpdateSchema


async def validate_create(user_service: UserServiceDep, user_create: UserCreateSchema) -> None:
    if user_service.get_by_username(user_create.username):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Username already exists')


async def validate_update(
    user_service: UserServiceDep, user_instance: UserModel, user_update: UserUpdateSchema
) -> None:
    if user_update.username != user_instance.username and user_service.get_by_username(user_update.username):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Username already exists')

    if user_update.email and user_update.email != user_instance.email and user_service.get_by_email(user_update.email):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Email already exists')
