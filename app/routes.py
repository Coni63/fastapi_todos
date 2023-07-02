from fastapi import APIRouter, HTTPException, status

from app.service.todo_item_service import TodoItemService
from app.todos.todo_item import TodoItem

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", tags=["todos"])
async def get_all_todos():
    all_items = TodoItemService.get_all_todos()
    return all_items


@router.get("/{id}", tags=["todos"])
async def get_todo_by_id(id: int):
    item = TodoItemService.get_todo_by_id(id)
    return item


@router.post("/create/", tags=["todos"], status_code=status.HTTP_201_CREATED)
async def read_item(new_item: TodoItem) -> bool:
    valid = TodoItemService.create_todo_item(new_item)
    if valid:
        return {"done": True}

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail='error while saving',
    )
