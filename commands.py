import json

from datetime import datetime

from models import Task, Session

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
       return e
    return data

def read_database():
    try:
        with open('db.json', 'r') as db:
            data = json.load(db)
    except FileNotFoundError as e:
        return e
    return data

def update_database(updated_data):
    try:
        with open('db.json', 'w') as db:
            json.dump(updated_data, db, indent=4)
    except FileNotFoundError as e:
        return e

#TASK-COMMANDS

def create_task(name):
    try:
        db = read_database()
        tasks = db["tasks"]
    except Exception as e:
        return e

    new_task = Task(name)
    new_task.entry_date = get_current_date()

    serialized_task = new_task.to_object()
    db["tasks"][name] = serialized_task
    
    updated_db = update_database(db)
    return new_task 

def read_task():
    pass

def update_task():
    pass

def delete_task():
    pass

def start_session(task):
    try:
        db = read_database()
        tasks = db["tasks"]
    except Exception as e:
        return e
    
    new_session = Session()
    new_session.start_time = get_current_date()

    serialized_session = new_session.to_object()
    task.sessions.append(serialized_session)

    return new_session

def end_session(task):
    pass





