import time
import sys
import schedule
import json
import signal
import os

from src import commands as c

args = sys.argv

class Tracker():
    def __init__(self):
        self.seppuku = False
        self.temp_storage = 'temp'
        self.log_file = os.path.join(self.temp_storage, 'tmp_log.txt')

    def logger(self):
        with open(self.log_file, 'w') as log:
            time = c.get_current_date()
            json.dump(time, log)
    
    def start(self, task_name:str):
        task = c.read_task(task_name)
        new_session = task.create_session()
        c.update_task(task)

        schedule.every(5).seconds.do(self.logger)

        while not self.seppuku:
            schedule.run_pending()
            time.sleep(1)

def handle_termination(self,signum, frame):
    tracker.seppuku = True

    with open(tracker.log_file, 'w') as log:
        time = c.get_current_date()
        flag = True
        data = [time, flag]
        json.dump(data, log)
        sys.exit(0)

signal.signal(signal.SIGTERM, handle_termination)
signal.signal(signal.SIGHUP, handle_termination)

if __name__ == "__main__":
    tracker = Tracker()
    tracker.start(args[1])
