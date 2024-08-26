from sqlalchemy.orm import Session

from ..dto.task_dto import TaskDto
from ..models.task import Task


def read_tasks(db: Session, page: int, limit: int):
    return db.query(Task).offset((page - 1) * limit).limit(limit).all()


def create_task(db: Session, taskDto: TaskDto):
    task = Task(**taskDto.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
