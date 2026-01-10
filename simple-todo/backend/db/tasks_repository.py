from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .orms import TasksORM


class TasksRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> List[TasksORM]:
        stmt = select(TasksORM)
        tasks = await self.session.scalars(stmt)
        return list(tasks.all())

    async def get_by_id(self, task_id: int) -> Optional[TasksORM]:
        stmt = select(TasksORM).where(TasksORM.task_id == task_id)
        task = await self.session.scalars(stmt)
        return task.one_or_none()

    async def create(self, text: str) -> TasksORM:
        task = TasksORM(text=text)
        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)
        return task

    async def update(self, task_id: int, new_text: str) -> Optional[TasksORM]:
        task = await self.get_by_id(task_id)
        if task is None:
            return None

        task.text = new_text
        await self.session.commit()
        await self.session.refresh(task)
        return task

    async def delete(self, task_id: int) -> bool:
        task = await self.get_by_id(task_id)
        if task is None:
            return False

        await self.session.delete(task)
        await self.session.commit()
        return True
