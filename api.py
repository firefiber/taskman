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

