from fastapi import APIRouter, HTTPException, status

from app import SQLiteSaver, TodoItem

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", tags=["todos"])
async def get_all_todos():
    saver = SQLiteSaver("database.db")
    all_items = saver.get_all_items()
    return all_items


@router.post("/create/", tags=["todos"], status_code=status.HTTP_201_CREATED)
async def read_item(new_item: TodoItem) -> bool:
    saver = SQLiteSaver("database.db")
    valid = saver.save(new_item)
    if valid:
        return True

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail='error while saving',
    )
