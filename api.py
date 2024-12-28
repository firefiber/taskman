import commands as c

import argparse
import subprocess
import psutil
import signal
import os
import time

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

start_task_tracking = subparsers.add_parser("start")
start_task_tracking.add_argument("task_name")

stop_task_tracking = subparsers.add_parser("stop")
stop_task_tracking.add_argument("task_name", nargs="?", help="Stop tracking a task.")

create_new_task = subparsers.add_parser("new")
create_new_task.add_argument("task_name")
create_new_task.add_argument("-s", "--structured", action="store_true", help="Structured list of tasks and subtasks.")

view_tasks = subparsers.add_parser("view")
view_tasks.add_argument("task_name", nargs="?", help="View task list")

args = parser.parse_args()

# print(f"API PID: {os.getpid()}, Parent PID: {os.getppid()}")

if args.command == "start":
    
    process = subprocess.Popen(["python", "tracker.py", args.task_name])
    
    with open("process.pid", 'w') as f:
        f.write(str(process.pid))

if args.command == "stop":
    # print(args.task_name)
    with open("process.pid", 'r') as f:
        pid = int(f.read().strip())
    
    process = psutil.Process(pid)
    process.terminate()

if args.command == "view":
    if args.task_name is not None:
        task = c.read_task(args.task_name)
        print(task)
    else:
        tasks = c.read_database()
        print([key for key in tasks.keys()])

if args.command == "new":
    if args.structured:
        pass
    else:
        try:
            c.create_task(args.task_name)
        except ValueError as e:
            print(e)
# Start the second script as a subprocess

# Main script continues doing its own thing
# while True:
#     print("Main script: Still working...")
#     time.sleep(2)  # Simulate some ongoing work

'''
if start:
    log tracker to file with periodic time entry

if stop:
    log to db with final time entry and flag set

if terminated:
    log to db with final time entry and no flag. 
'''