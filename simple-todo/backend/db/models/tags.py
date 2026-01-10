from typing import List, TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from db.base import Base, primary_key, unique_str

if TYPE_CHECKING:
    from .tasks import TasksORM


class TagsORM(Base):
    __tablename__ = "tags"

    tag_id: Mapped[primary_key]
    name: Mapped[unique_str]

    tasks: Mapped[List["TasksORM"]] = relationship(
        back_populates="tags", secondary="task_tag"
    )
