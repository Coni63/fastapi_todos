import unittest

# The fact that we import Model that inherit from sqlalchemy Base, add them to the Base and will be created
from app.repository.models.todo_item_model import TodoItemModel
from app.repository.database import engine, Base

from app.todos.todo_item import TodoItem
from app.service.todo_item_service import TodoItemService



class TestTodoService(unittest.TestCase):
    def setUp(self) -> None:
        Base.metadata.create_all(engine)

        for i in range(10):
            item = TodoItem(title=f"item{i}", description=f"description{i}")
            TodoItemService.create_todo_item(item)

    def test_create_item(self):
        todos = TodoItemService.get_all_todos()
        self.assertEqual(len(todos), 10)

        item = TodoItem(title=f"item11", description=f"description11")
        TodoItemService.create_todo_item(item)

        todos = TodoItemService.get_all_todos()
        self.assertEqual(len(todos), 11)
        self.assertIsInstance(todos[-1], TodoItem)
        self.assertEqual(todos[-1].title, item.title)

    def test_get_todos_item(self):
        todos = TodoItemService.get_all_todos()
        self.assertEqual(len(todos), 11)
        self.assertIsInstance(todos[0], TodoItem)
