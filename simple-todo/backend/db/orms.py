from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text, DateTime, func
from typing import List, Annotated
from datetime import datetime


primary_key = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
unique_str = Annotated[str, mapped_column(unique=True)]


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


class TaskTagORM(Base):
    __tablename__ = "task_tag"

    task_fk: Mapped[int] = mapped_column(
        ForeignKey("tasks.task_id"), primary_key=True, ondelete="CASCADE"
    )
    tag_fk: Mapped[int] = mapped_column(
        ForeignKey("tags.tag_id"), primary_key=True, ondelete="CASCADE"
    )


class TagsORM(Base):
    __tablename__ = "tags"

    tag_id: Mapped[primary_key]
    name: Mapped[unique_str]

    tasks: Mapped[List["TasksORM"]] = relationship(
        back_populates="tags", secondary="task_tag"
    )


class StatusesORM(Base):
    __tablename__ = "statuses"

    status_id: Mapped[primary_key]
    name: Mapped[unique_str]

    tasks: Mapped[List["TasksORM"]] = relationship(back_populates="status")
