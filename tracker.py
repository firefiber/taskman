import time
import sys
import commands as c

args = sys.argv

class Tracker():
    def start(self, task_name:str):
        task = c.read_task(task_name)
        # print(task)
        new_session = task.create_session()
        print(task)
        c.update_task(task)
        print(task)
        
        # c.update_database(task)
    
if __name__ == "__main__":
    tracker = Tracker()
    tracker.start(args[1])