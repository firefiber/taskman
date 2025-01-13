# import sqlite3
# from src import models
# class Database:
#     def __init__(self):
#         self.conn = sqlite3.connect('data/taskman.db')
#         self.conn.row_factory = sqlite3.Row
#         self.cursor = self.conn.cursor()

#     def create_user(self, **kwargs):
#         username = kwargs.get("username")
#         email = kwargs.get("email")
#         password = kwargs.get("password")
#         is_activated = 1 if username is not None else 0

#         self.cursor.execute(
#             """
#             INSERT INTO Users (username, email, password, is_activated)
#             Values (?, ?, ?, ?)
#             """,
#             (username, email, password, is_activated)
#         )

#         self.conn.commit()

#     def delete_user(self, **kwargs):
#         id = kwargs.get("id")

#         self.cursor.execute(
#             """
#             DELETE FROM Users WHERE id = ?
#             """,
#             (id,)
#         )

#         self.conn.commit()

#     def create_task(self, **kwargs):
#         name = kwargs.get("name")
#         description = kwargs.get("description")
#         owner_id = kwargs.get("owner_id")

#         self.cursor.execute(
#             """
#             INSERT INTO Tasks (name, description, owner_id)
#             Values (?, ?, ?)
#             RETURNING *
#             """,
#             (name, description, owner_id)
#         )

#         row = self.cursor.fetchone()
#         task = models.Task(**row)
#         return task


#     def get_user(self, **kwargs):
#         id = kwargs.get("id")

#         self.cursor.execute(
#             """
#             SELECT * FROM Users WHERE id = ?
#             """,
#             (id,)
#         )
        
#         row = self.cursor.fetchone()
#         user = models.User(**row)
#         return user

from datetime import datetime
from typing import Optional
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, declarative_base, relationship
import uuid

db = create_engine('sqlite:///taskman.db')
Session = sessionmaker(bind=db)
Base = declarative_base()


def generate_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = 'Users'
    id: Mapped[str] = mapped_column(primary_key=True, index=True, unique=True, default=generate_uuid)
    username: Mapped[Optional[str]]
    email: Mapped[Optional[str]]
    password: Mapped[Optional[str]]

class Task(Base):
    __tablename__ = 'Tasks'
    id: Mapped[str] = mapped_column(primary_key=True, index=True, unique=True, default=generate_uuid)
    name: Mapped[str] = mapped_column(index=True)
    description: Mapped[Optional[str]]
    done: Mapped[bool] = mapped_column(default=False)
    owner_id: Mapped[str] = mapped_column(ForeignKey('Users.id'))
    entry_date: Mapped[datetime] = mapped_column(default=datetime.now)
    start_date: Mapped[Optional[datetime]]
    end_date: Mapped[Optional[datetime]]
    total_duration: Mapped[str] = mapped_column(default="0.0")
    dependencies = relationship("Task", secondary="Dependencies", backref="dependents")

class Dependencies(Base):
    __tablename__ = 'Dependencies'
    task_id: Mapped[str] = mapped_column(ForeignKey('Tasks.id'), primary_key=True)
    depends_on_id: Mapped[str] = mapped_column(ForeignKey('Tasks.id'), primary_key=True)


    
if __name__ == "__main__":
    Base.metadata.create_all(db)
    session = Session()

    # new_user = User()
    # session.add(new_user)
    # session.commit()
    # newTask = Task(name="test_task", owner_id=new_user.id)
    # session.add(newTask)
    # user = session.query(User).first()
    # new_task = Task(name="usage_goals", owner_id=user.id)
    # session.add(new_task)

    context = session.query(Task).filter(Task.name == "taskman_app").first()
    dependency = session.query(Task).filter(Task.name == "usage_goals").first()

    new_dependency = Dependencies(task_id=context.id, depends_on_id=dependency.id)

    session.add(new_dependency)

    session.commit()

    



