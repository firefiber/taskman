import sqlite3
from src import models
class Database:
    def __init__(self):
        self.conn = sqlite3.connect('data/taskman.db')
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def create_user(self, **kwargs):
        username = kwargs.get("username")
        email = kwargs.get("email")
        password = kwargs.get("password")
        is_activated = 1 if username is not None else 0

        self.cursor.execute(
            """
            INSERT INTO Users (username, email, password, is_activated)
            Values (?, ?, ?, ?)
            """,
            (username, email, password, is_activated)
        )

        self.conn.commit()

    def delete_user(self, **kwargs):
        id = kwargs.get("id")

        self.cursor.execute(
            """
            DELETE FROM Users WHERE id = ?
            """,
            (id,)
        )

        self.conn.commit()

    def create_task(self, **kwargs):
        name = kwargs.get("name")
        description = kwargs.get("description")
        owner_id = kwargs.get("owner_id")

        self.cursor.execute(
            """
            INSERT INTO Tasks (name, description, owner_id)
            Values (?, ?, ?)
            RETURNING *
            """,
            (name, description, owner_id)
        )

        row = self.cursor.fetchone()
        task = models.Task(**row)
        return task


    def get_user(self, **kwargs):
        id = kwargs.get("id")

        self.cursor.execute(
            """
            SELECT * FROM Users WHERE id = ?
            """,
            (id,)
        )
        
        row = self.cursor.fetchone()
        user = models.User(**row)
        return user

if __name__ == "__main__":
    db = Database()
    new_user = {
        "username": "test_user"
    }
    # db.create_user(username="test_user2")
    db.create_user()

# conn = sqlite3.connect('data/taskman.db')
# cursor = conn.cursor()

# cursor.execute('''
#     SELECT * FROM Tasks;
# ''')

# rows = cursor.fetchall()
# for row in rows:
#     print(row)