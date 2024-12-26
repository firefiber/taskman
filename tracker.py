import time
import sys
import schedule
import json
import signal

import commands as c

args = sys.argv

class Tracker():
    def __init__(self):
        self.seppuku = False

    def logger(self):
        with open('.tmp_log.txt', 'w') as log:
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

def handle_termination(signum, frame):
    tracker.seppuku = True
    with open('.tmp_log.txt', 'w') as log:
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
