from datetime import datetime
from typing import List, TYPE_CHECKING

from sqlalchemy import Text, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base, primary_key, unique_str

if TYPE_CHECKING:
    from db.models import StatusesORM, TagsORM


class TasksORM(Base):
    __tablename__ = "tasks"

    task_id: Mapped[primary_key]
    title: Mapped[unique_str]
    description: Mapped[str] = mapped_column(Text, nullable=True)
    due_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), server_onupdate=func.now()
    )

    status_id: Mapped[int] = mapped_column(ForeignKey("statuses.status_id"), index=True)
    status: Mapped["StatusesORM"] = relationship(back_populates="tasks")

    tags: Mapped[List["TagsORM"]] = relationship(
        back_populates="tasks", secondary="task_tag"
    )
