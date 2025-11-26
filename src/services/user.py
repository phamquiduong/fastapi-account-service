import uuid

from sqlmodel import Session, select

from models.user import UserModel
from schemas.user.create import UserCreateSchema
from schemas.user.update import UserUpdateSchema
from services.password import PasswordService


class UserService:
    def __init__(self, session: Session, password_service: PasswordService) -> None:
        self.session = session
        self.password_service = password_service

    def get_by_id(self, user_id: str) -> UserModel | None:
        return self.session.get(UserModel, uuid.UUID(user_id))

    def get_by_username(self, username: str) -> UserModel | None:
        return self.session.exec(select(UserModel).where(UserModel.username == username)).first()

    def get_by_email(self, email: str) -> UserModel | None:
        return self.session.exec(select(UserModel).where(UserModel.email == email)).first()

    def get_all(self, limit: int = 100, offset: int = 0) -> list[UserModel]:
        users = self.session.exec(select(UserModel).offset(offset).limit(limit)).all()
        return list(users)

    def create(self, user_create: UserCreateSchema) -> UserModel:
        user_create.password = self.password_service.get_password_hash(user_create.password)

        user_model = UserModel.model_validate(user_create.model_dump())
        self.session.add(user_model)
        self.session.commit()
        self.session.refresh(user_model)

        return user_model

    def update(self, user_instance: UserModel, user_update: UserUpdateSchema) -> UserModel:
        if user_instance.email != user_update.email:
            user_instance.email_verified = False
        user_instance.sqlmodel_update(user_update.model_dump(exclude_unset=True))

        self.session.add(user_instance)
        self.session.commit()
        self.session.refresh(user_instance)

        return user_instance
