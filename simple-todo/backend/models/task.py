from pydantic import BaseModel, ConfigDict


class TaskCreate(BaseModel):
    text: str


class TaskRead(TaskCreate):
    id: int
    is_complete: bool

    model_config = ConfigDict(from_attributes=True)
