from sqlmodel import Session

from models.user import UserModel
from schemas.user.create import UserCreateSchema
from services.password import PasswordService


class UserService:
    def __init__(self, session: Session, password_service: PasswordService) -> None:
        self.session = session
        self.password_service = password_service

    def create(self, user_create: UserCreateSchema) -> UserModel:
        user_create.password = self.password_service.get_password_hash(user_create.password)

        user_model = UserModel.model_validate(user_create.model_dump())
        self.session.add(user_model)
        self.session.commit()
        self.session.refresh(user_model)

        return user_model
