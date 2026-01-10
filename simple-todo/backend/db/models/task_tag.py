from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base


class TaskTagORM(Base):
    __tablename__ = "task_tag"

    task_fk: Mapped[int] = mapped_column(
        ForeignKey("tasks.task_id", ondelete="CASCADE"), primary_key=True
    )
    tag_fk: Mapped[int] = mapped_column(
        ForeignKey("tags.tag_id", ondelete="CASCADE"), primary_key=True
    )
