from fastapi import APIRouter

from ..controllers import task_controller

router = APIRouter()


@router.get("/")
async def read_tasks():
    return task_controller.read_tasks()
