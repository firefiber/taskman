import json

from datetime import datetime

from src.models import Task, Session

#GENERAL

def get_current_date():
    date = datetime.now().isoformat()
    return date

#DATABASE

def create_database():
    try:
        with open('db.json', 'x') as db:
            data = {"tasks": {}}
            json.dump(data, db)
    except FileExistsError as e:
       raise e
    return data

def read_database():
    try:
        with open('db.json', 'r') as db:
            data = json.load(db)
    except FileNotFoundError as e:
        raise e
    tasks = data["tasks"]
    return tasks

def update_database(updated_data):
    try:
        with open('db.json', 'w') as db:
            data = {"tasks": updated_data}
            json.dump(data, db, indent=4)
    except FileNotFoundError as e:
        raise e

#TASK-COMMANDS

def create_task(task_name: str):
    all_tasks = read_database()
    new_task = Task(name=task_name)

    if task_name in all_tasks:
        raise ValueError("Task already exists.")
    else:
        all_tasks[task_name] = new_task.model_dump()
    
    update_database(all_tasks)
    
    return new_task 

def read_task(task_name: str):
    try: 
        tasks = read_database()
        selected_task = Task(**tasks[task_name])
    except KeyError as e:
        return f"No task found with name: {task_name}."
    except Exception as e:
        raise e
    
    return selected_task

def update_task(task: Task):
    all_tasks = read_database()
    all_tasks[task.name] = task.model_dump() 

    update_database(all_tasks)

def delete_task():
    pass

def start_session() -> Session:
    new_session = Session()
    new_session.start_time = get_current_date()

    return new_session

def end_session(task):
    pass





