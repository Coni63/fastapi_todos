import sqlite3

from app.saver import ISaver
from app.todos import TodoItem


class SQLiteSaver(ISaver):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.con = sqlite3.connect(file_path)
        self.cur = self.con.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS todos(id INTEGER PRIMARY KEY, title TEXT , description TEXT , created_at TEXT, status INTEGER)")

    def __del__(self):
        self.cur.close()
        self.con.close()

    def save(self, item: TodoItem) -> bool:
        # try:
        data = (item.id, item.title, item.description, item.created_at.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3], item.status.value)
        print(data)
        self.cur.execute("INSERT INTO todos VALUES(?, ?, ?, ?, ?)", data)
        self.con.commit()
        return True
        # except Exception as e:
        #     return False

    def get_all_items(self) -> list[TodoItem]:
        res = self.cur.execute("""
            SELECT id, title , description, created_at, status
            FROM todos
            ORDER BY created_at DESC
        """)
        return [
            TodoItem(
                id=id,
                title=title,
                description=description,
                created_at=created_at,
                status=status
            )
            for id, title, description, created_at, status in res
        ]

    def update(self, item: TodoItem) -> TodoItem:
        return item
