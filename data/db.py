import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('data/taskman.db')
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