from datetime import datetime
import json
from data.db import get_or_create
from data.models import Base, db, get_session, User, Task, Dependencies, DependencyType
from .structure import parse_hierarchy
from icecream import ic
import argparse
import uuid


def start_task(args):
    session = get_session()
    task = session.query(Task).filter_by(name=args.task_name).first()
    if task:
        task.start_date = datetime.now()
        session.commit()
        print(f"Task '{args.task_name}' started.")
    else:
        print(f"Task '{args.task_name}' not found.")
    session.close()

def stop_task(args):
    session = get_session()
    task = session.query(Task).filter_by(name=args.task_name).first()
    if task:
        task.end_date = datetime.now()
        task.done = True
        session.commit()
        print(f"Task '{args.task_name}' stopped.")
    else:
        print(f"Task '{args.task_name}' not found.")
    session.close()

def view_tasks(args):
    session = get_session()
    user = session.query(User).filter_by(username="admin").first()

    if not args.task_name:
        current_context = session.query(Task).filter_by(name=user.id).first()
    else:
        current_context = session.query(Task).filter_by(name=args.task_name).first()
    
    dependencies = session.query(Dependencies).filter_by(context=current_context.id).all()


    for dependency in dependencies:
        task = session.query(Task).filter_by(id=dependency.task_id).first()
        ic(current_context.name, task.name)
    # if args.task_name:
    #     task = session.query(Task).filter_by(name=args.task_name).first()
    #     if task:
    #         print(task)
    #     else:
    #         print(f"Task '{args.task_name}' not found.")
    # else:
    #     tasks = user.tasks

    #     for task in tasks:
    #         print(task.name)
    session.close()

def create_new_task(args):
    session = get_session()

    user = session.query(User).filter_by(username="admin").first()
    context = session.query(Task).filter_by(id=user.id).first()

    dependency_type = DependencyType.INTERNAL

    try:
        tasks_hierarchy = parse_hierarchy(args.task_name)

        # Initialize auto-incrementing counters
        entry_order = 1
        dependency_order = 1

        def create_tasks(task_dict, context, entry_order, dependency_order):
            """
            Recursive function to create tasks and their dependencies.
            """
            for task_name, subtasks in task_dict.items():
                ic(task_name, entry_order, dependency_order)
                # Create the task
                new_task = Task(name=task_name, owner_id=user.id)
                session.add(new_task)
                session.commit()

                # Add the dependency
                dependency = Dependencies(
                    context=context.id,
                    task_id=new_task.id,
                    dependency_type=dependency_type,
                    entry_order=entry_order,
                    dependency_order=dependency_order,
                )
                session.add(dependency)
                session.commit()

                # Recursively handle subtasks
                if subtasks not in (None, []):
                    entry_order, dependency_order = (1, 1)
                    for subtask in subtasks:
                        context = new_task
                        create_tasks(subtask, context, entry_order, dependency_order)

                        entry_order += 1
                        dependency_order += 1

        # Process each top-level task dictionary
        for task_dict in tasks_hierarchy:
            create_tasks(task_dict, context, entry_order, dependency_order)

            entry_order += 1
            dependency_order += 1

        print("Tasks created successfully.")

    except Exception as e:
        print(f"Error creating tasks: {e}")
        session.rollback()
    finally:
        session.close()

def create_database(args):
    Base.metadata.create_all(db)
    session = get_session()
    # generate uuid for default user with correct imports
    unique_id = str(uuid.uuid4())
    print(unique_id)

    default_user = User(id=unique_id, username="admin")
    session.add(default_user)
    root_context = Task(id=unique_id, owner_id=default_user.id, name=unique_id)
    session.add(root_context)
    session.commit()
    print("Database created")

def add_dependency(args):
    session = get_session()
    task = session.query(Task).filter_by(name=args.task_name).first()
    dependencies = session.query(Task).filter(Task.name.in_(args.dependencies)).all()
    if task and dependencies:
        task.dependencies.extend(dependencies)
        session.commit()
        print(f"Dependencies added to '{args.task_name}'")
    else:
        print(f"Task or dependencies not found.")
    session.close()

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

create_db_parser = subparsers.add_parser("create_db", help="Create the database")

start_task_tracking = subparsers.add_parser("start")
start_task_tracking.add_argument("task_name")

stop_task_tracking = subparsers.add_parser("stop")
stop_task_tracking.add_argument("task_name", nargs="?", help="Stop tracking a task.")

create_new_task_parser = subparsers.add_parser("new")
create_new_task_parser.add_argument("task_name")

view_tasks_parser = subparsers.add_parser("view")
view_tasks_parser.add_argument("task_name", nargs="?", help="View task list")

add_dependency_parser = subparsers.add_parser("add_dependency", help="Add dependencies to a task")
add_dependency_parser.add_argument("task_name")
add_dependency_parser.add_argument("dependencies", nargs='+', help="List of task names to add as dependencies")

args = parser.parse_args()

command_mapping = {
    "start": start_task,
    "stop": stop_task,
    "view": view_tasks,
    "new": create_new_task,
    "create_db": create_database,
    "add_dependency": add_dependency
}

if args.command in command_mapping:
    command_mapping[args.command](args)
else:
    parser.print_help()