import commands as c

import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

start_parser = subparsers.add_parser("new")
start_parser.add_argument("task_name", nargs="?", help="Create a new task.")
start_parser.add_argument('-s', '--structured', action="store_true", help="Structured list of tasks and subtasks.")

args = parser.parse_args()

if args.command == "new":
    new_task = c.create_task(args.task_name)

import subprocess
import time

# Start the second script as a subprocess
process = subprocess.Popen(["python", "tracker.py", "test"])

print("Main script: Started the worker script!")

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