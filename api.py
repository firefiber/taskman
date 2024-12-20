import commands as c

import argparse
import subprocess
import psutil
import signal
import os
import time

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

start_parser = subparsers.add_parser("start")
start_parser.add_argument("task_name", nargs="?", help="Start tracking a task.")
# start_parser.add_argument('-s', '--structured', action="store_true", help="Structured list of tasks and subtasks.")

stop_parser = subparsers.add_parser("stop")
start_parser.add_argument("task_name", nargs="?", help="Stop tracking a task.")

args = parser.parse_args()

if args.command == "start":
    process = subprocess.Popen(["python", "tracker.py", "test"])
    
    with open("process.pid", 'w') as f:
        f.write(str(process.pid))

if args.command == "stop":
    with open("process.pid", 'r') as f:
        pid = int(f.read().strip())
    
    process = psutil.Process(pid)
    process.terminate()

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