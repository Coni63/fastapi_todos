# flake8: noqa
from app.repository.models.todo_item_model import TodoItemModel
from app.repository.database import engine, Base
from app.todos.todo_item import TodoItem
from app.service.todo_item_service import TodoItemService

Base.metadata.create_all(engine)

for i in range(10):
    item = TodoItem(title="item{i}", description="description{i}")
    TodoItemService.create_todo_item(item)