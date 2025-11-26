from fastapi import APIRouter, Depends, status

from dependencies.user import UserFromPathDep, UserServiceDep
from models.user import UserModel
from schemas.user.create import UserCreateSchema
from schemas.user.update import UserUpdateSchema
from validators import user

user_router = APIRouter(prefix='/users', tags=['Users'])


@user_router.get('/')
async def get_all_users(
    user_service: UserServiceDep,
    limit: int = 100,
    offset: int = 0
) -> list[UserModel]:
    return user_service.get_all(limit=limit, offset=offset)


@user_router.post('/register', status_code=status.HTTP_201_CREATED)
async def register_user(
    user_create: UserCreateSchema,
    # Dependencies
    user_service: UserServiceDep,
    # DB Validate and Permissions
    db_valid=Depends(user.validate_create)
) -> UserModel:
    return user_service.create(user_create)


@user_router.put('/{user_id}', status_code=status.HTTP_200_OK)
async def update_user(
    user_id: str,
    user_update: UserUpdateSchema,
    # Dependencies
    user_service: UserServiceDep,
    user_instance: UserFromPathDep,
    # DB Validate and Permissions
    db_valid=Depends(user.validate_update)
) -> UserModel:
    return user_service.update(user_instance, user_update)
