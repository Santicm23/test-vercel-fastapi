from pydantic import BaseModel


class TaskDto(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        orm_mode = True