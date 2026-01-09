from pydantic import BaseModel


class TaskCreate(BaseModel):
    text: str


class TaskRead(TaskCreate):
    id: int
    is_complete: bool
