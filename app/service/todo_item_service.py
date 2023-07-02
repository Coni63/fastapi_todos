from app.repository.models.todo_item_model import TodoItemModel
from app.todos import TodoItem

from app.repository.database import SessionLocal


class TodoItemService:
    @staticmethod
    def get_all_todos() -> list[TodoItem]:
        session = SessionLocal()
        ans = [TodoItem.from_orm(item) for item in session.query(TodoItemModel).all()]
        session.close()
        return ans

    @staticmethod
    def get_todo_by_id(id: int) -> TodoItem:
        session = SessionLocal()
        record = session.query(TodoItemModel).get(id)
        session.close()
        return TodoItem.from_orm(record)

    @staticmethod
    def update_todo_by_id(id: int) -> TodoItem:
        pass

    @staticmethod
    def patch_todo_by_id(id: int) -> TodoItem:
        pass

    @staticmethod
    def delete_todo_by_id(id: int):
        pass

    @staticmethod
    def create_todo_item(data: TodoItem) -> bool:
        session = SessionLocal()
        new_item = TodoItemModel(**data.as_dict())
        session.add(new_item)
        session.commit()
        session.close()
