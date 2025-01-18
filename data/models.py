from datetime import datetime
from typing import Optional
from sqlalchemy import create_engine, ForeignKey, Enum
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, declarative_base, relationship
import uuid
import enum

db = create_engine('sqlite:///data/taskman.db')
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
    tasks: Mapped[list["Task"]] = relationship("Task", uselist=True)

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

class DependencyType(enum.Enum):
    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"

class Dependencies(Base):
    __tablename__ = 'Dependencies'
    context: Mapped[str] = mapped_column(ForeignKey('Tasks.id'), primary_key=True)
    task_id: Mapped[str] = mapped_column(ForeignKey('Tasks.id'), primary_key=True)
    dependency_type: Mapped[DependencyType] = mapped_column(Enum(DependencyType), default=DependencyType.EXTERNAL)
    dependency_order: Mapped[int] = mapped_column(default=0)
    entry_order: Mapped[int] = mapped_column(default=0)

def get_session():
    return Session()
    
if __name__ == "__main__":
    Base.metadata.create_all(db)








