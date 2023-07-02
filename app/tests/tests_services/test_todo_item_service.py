import unittest

from app.repository.database import engine, Base
from app.repository.models.todo_item_model import TodoItemModel
from app.todos.todo_item import TodoItem
from app.service.todo_item_service import TodoItemService



class TestTodoService(unittest.TestCase):
    def setUp(self) -> None:
        Base.metadata.create_all(engine)

        for i in range(10):
            item = TodoItem(title=f"item{i}", description=f"description{i}")
            TodoItemService.create_todo_item(item)

    def test_create_item(self):
        ans = TodoItemService.get_all_todos()
        self.assertEqual(len(ans), 10)