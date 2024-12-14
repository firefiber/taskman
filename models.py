from __future__ import annotations
from datetime import datetime
from typing import Optional


class BaseCommand():
    pass


def get_current_date():
    current_date = datetime.now().isoformat()
    return current_date


class ControlPanel():
    def create_task():
        pass

    def load_task():
        pass

    def delete_task():
        pass

    def update_task():
        pass

    def start_session():
        pass

    def end_session():
        pass


class Task:
    def __init__(self, name: str, parent: Optional[Task] = None):
        self.name = name
        self.parent = parent
        self.entry_date: str = None
        self.begin_date: str = None
        self.end_date: str = None
        self.sessions: list[dict] = []
        self.sub_tasks: list[Task] = []
        self.total_duration: float = 0.0
        self.done: bool = False

    def set_entry_date(self):
        self.entry_date = get_current_date()
    
    def create_session(self):
        new_session = Session()
        new_session.start_time = get_current_date()      
        self.sessions.append(new_session.to_object())

    def end_session(self, session):
        session.end_time = get_current_date()

    def to_object(self):
        return {
            "parent": self.parent,
            "entry_date": self.entry_date,
            "begin_date": self.begin_date,
            "end_date": self.end_date,
            "sessions": self.sessions,
            "sub_tasks": self.sub_tasks,
            "total_duration": self.total_duration,
            "done": self.done
        }
    
    def __repr__(self):
        return f"name: {self.name}\nparent: {self.parent}\nentry_date: {self.entry_date}"
    
class Session:
    def __init__(self):
        self.start_time: str = None
        self.end_time: str = None
        self.duration: float = 0.0
        self.was_manually_stopped: bool = False

    def to_object(self):
        return {
            "start_time": self.start_time,
            "end_time": self.end_time,
            "duration": self.duration,
            "was_manually_stopped": self.was_manually_stopped
        }
