import sys
from typing import List, Dict
import re
from icecream import ic

def parse_task_tree(task_string):
    """
    Parses a single task tree from the given string and builds a hierarchical structure.
    """
    tokens = task_string.strip().split(">")
    stack = []
    root = []

    current_context = root
    for token in tokens:
        token = token.strip()  # Clean up whitespace
        if not token:
            continue

        subtasks = [sub.strip() for sub in token.split(",") if sub.strip()]
        for subtask in subtasks:
            task_obj = {subtask: []}
            current_context.append(task_obj)

        # Move down a level for the last task in this token
        if subtasks:
            stack.append(current_context)
            current_context = current_context[-1][subtasks[-1]]

    # Handle moving back up levels
    while stack:
        current_context = stack.pop()

    return root

def parse_hierarchy(input_string):
    """
    Parses the input string into a hierarchy of tasks.
    """
    task_trees = input_string.split(";")
    root = []

    for task_tree in task_trees:
        task_tree = task_tree.strip()
        if not task_tree:
            continue

        # Parse the individual task tree and append it to the root
        parsed_tree = parse_task_tree(task_tree)
        root.extend(parsed_tree)

    return root

if __name__ == "__main__":
    input_str = sys.argv[1]
    tasks = parse_hierarchy(input_str)
    print(tasks)
