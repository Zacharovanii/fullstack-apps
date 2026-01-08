from fastapi import APIRouter
from core import get_settings

s = get_settings()
router = APIRouter(
    tags=[s.api.v1.tasks, s.api.v1.prefix], prefix=f"{s.api.prefix}{s.api.v1.prefix}"
)


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
