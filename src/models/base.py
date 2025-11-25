import uuid
from datetime import datetime

from sqlmodel import Field, SQLModel

from utils import timezone


class BaseModel(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=timezone.now)
    updated_at: datetime = Field(default_factory=timezone.now)
