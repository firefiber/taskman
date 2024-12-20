from __future__ import annotations
from icecream import ic
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, field_validator

def get_current_date():
    current_date = datetime.now().isoformat()
    return current_date


class Task(BaseModel):
    name: str
    context: Optional[str] = None
    entry_date: str = get_current_date()
    done: bool = False
    begin_date: Optional[str] = None
    end_date: Optional[str] = None
    sessions: Optional[list[Session]] = []
    super_tasks: Optional[list[Task]] = []
    sub_tasks: Optional[list[Task]] = []
    total_duration: float = 0.0

    def get_field(self, field):
        return getattr(self, field)
    
    def create_session(self):
        new_session = Session(
            start_time = get_current_date()
        )
        print(new_session)
        self.sessions.append(new_session)

        return new_session

    def __repr__(self):
        return self.name 
      
class Session(BaseModel):
    start_time: str = None
    end_time: Optional[str] = None
    duration: Optional[float] = 0.0
    was_manually_stopped: bool = False

    
