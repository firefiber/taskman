from __future__ import annotations
from icecream import ic
from datetime import datetime, timedelta
from typing import Optional, Literal
from enum import Enum
from pydantic import BaseModel, field_validator

def get_current_date():
    current_date = datetime.now().isoformat()
    return current_date


class Task(BaseModel):
    name: str
    context: Optional[str] = None
    entry_date: str = get_current_date()
    done: bool = False
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    sessions: Optional[list[Session]] = []
    dependants: Optional[list[Task]] = []
    dependencies: Optional[list[Task]] = []
    total_duration: float = 0.0

    def get_field(self, field):
        return getattr(self, field)
    
    def create_session(self):
        new_session = Session(
            start_time = get_current_date()
        )
        self.sessions.append(new_session)

        return new_session

    # def __repr__(self):
    #     return self.name 
      
class Session(BaseModel):
    start_time: str = None
    end_time: Optional[str] = None
    duration: Optional[float] = 0.0
    was_manually_stopped: bool = False


'''
schedule by:
    - Duration (seconds, minutes, hours, days, months, years)
    - 
'''
    
class Block(BaseModel):
    task: Task
    size: Optional[timedelta]
    basis: Optional[Literal["entry", "start", "custom"]]

    # def compute_remanining_size(self):
    #     if self.origin == "entry":
    #         from_date = datetime.fromisoformat(self.task.entry_date)
    #     elif self.origin == "start":
    #         if not self.task.start_date:
    #             raise ValueError("Task not yet started.")
    #         from_date = datetime.fromisoformat(self.task.start_date)
    #     else:
    #         return "No size set for this task."
    
    #     return self.size - 