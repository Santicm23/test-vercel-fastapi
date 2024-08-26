from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..config.db.sqlite import SessionLocal
from ..controllers import task_controller
from ..dto.task_dto import TaskDto

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[TaskDto])
async def read_tasks(page: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return task_controller.read_tasks(db, page, limit)


@router.post("/", response_model=TaskDto)
async def create_task(task: TaskDto, db: Session = Depends(get_db)):
    return task_controller.create_task(db, task)
