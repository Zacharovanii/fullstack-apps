from typing import Annotated

from fastapi import APIRouter, Depends
from core import get_settings


# TEST DEPS
from db import db_helper
from db.tasks import TaskORM

from sqlalchemy.ext.asyncio import AsyncSession

s = get_settings()
router = APIRouter(
    tags=[s.api.v1.tasks, s.api.v1.prefix], prefix=f"{s.api.prefix}{s.api.v1.prefix}"
)


@router.post("/tasks/test")
async def test_task_create(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    text: str,
):
    task = TaskORM(text=text)
    session.add(task)
    await session.commit()
    return {"data": task}


@router.get("/tasks")
def get_all_tasks():
    return {"data": "All tasks"}


@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    return {"data": f"Task id: {task_id}"}


@router.post("/tasks")
def create_task(text: str):
    return {"data": f"Task text: {text}"}


@router.patch("/tasks/{task_id}")
def update_task(task_id: int, text: str):
    return {"data": f"Task text: {text}, id: {task_id}"}


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    return {"data": f"Task delete: {task_id}"}
