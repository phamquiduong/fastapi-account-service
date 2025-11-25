from typing import Annotated

from fastapi import Depends

from services.password import PasswordService


def get_password_service():
    yield PasswordService()


PasswordServiceDep = Annotated[PasswordService, Depends(get_password_service)]
