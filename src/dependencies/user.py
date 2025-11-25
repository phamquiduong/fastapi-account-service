from typing import Annotated

from fastapi.params import Depends

from dependencies.password import PasswordServiceDep
from dependencies.session import SessionDep
from services.user import UserService


async def get_user_service(session: SessionDep, password_service: PasswordServiceDep):
    yield UserService(session=session, password_service=password_service)

UserServiceDep = Annotated[UserService, Depends(get_user_service)]
