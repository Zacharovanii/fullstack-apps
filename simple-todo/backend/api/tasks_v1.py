from typing import Annotated, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core import get_settings
from db import db_helper
from db.tasks_repository import TasksRepository
from models import TaskRead, TaskCreate

s = get_settings()
router = APIRouter(
    tags=[s.api.v1.tasks, s.api.v1.prefix], prefix=f"{s.api.prefix}{s.api.v1.prefix}"
)

SESSION_DEPENDENCY = Annotated[AsyncSession, Depends(db_helper.session_getter)]


@router.get("/tasks")
async def get_all_tasks(session: SESSION_DEPENDENCY) -> List[TaskRead]:
    tr = TasksRepository(session)
    tasks = await tr.get_all()
    return [TaskRead.model_validate(task) for task in tasks]


@router.get("/tasks/{task_id}")
async def get_task(session: SESSION_DEPENDENCY, task_id: int) -> Optional[TaskRead]:
    tr = TasksRepository(session)
    task = await tr.get_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskRead.model_validate(task)


@router.post("/tasks")
async def create_task(session: SESSION_DEPENDENCY, task: TaskCreate) -> TaskRead:
    tr = TasksRepository(session)
    task = await tr.create(task.text)
    return TaskRead.model_validate(task)


@router.patch("/tasks/{task_id}")
async def update_task(
    session: SESSION_DEPENDENCY, task: TaskCreate, task_id: int
) -> TaskRead:
    tr = TasksRepository(session)
    task = await tr.update(task_id=task_id, new_text=task.text)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskRead.model_validate(task)


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(session: SESSION_DEPENDENCY, task_id: int):
    tr = TasksRepository(session)
    deleted = await tr.delete(task_id=task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
