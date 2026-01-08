from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text


class TaskORM(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    is_complete: Mapped[bool] = mapped_column(default=False, server_default="false")
