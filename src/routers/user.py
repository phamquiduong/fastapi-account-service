from fastapi import APIRouter, status

from dependencies.user import UserServiceDep
from models.user import UserModel
from schemas.user.create import UserCreateSchema

user_router = APIRouter(prefix='/users', tags=['Users'])


@user_router.post('/register', status_code=status.HTTP_201_CREATED)
async def register_user(
    user_service: UserServiceDep,
    user_create: UserCreateSchema
) -> UserModel:
    return user_service.create(user_create)
