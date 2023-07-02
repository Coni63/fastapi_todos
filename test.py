from app.service.todo_item_service import TodoItemService
from app.todos.todo_item import TodoItem

# item = TodoItem(title="toto", description="desc")

# TodoItemService.create_todo_item(item)

# print(TodoItemService.get_all_todos())
print(TodoItemService.get_todo_by_id(2))
