import time
import sys
import schedule
import json

import commands as c

args = sys.argv

class Tracker():
    def logger(self):
        with open('.tmp_log.txt', 'w') as log:
            time = c.get_current_date()
            json.dump(time, log)
    
    def start(self, task_name:str):
        task = c.read_task(task_name)
        new_session = task.create_session()
        c.update_task(task)

        schedule.every(5).seconds.do(self.logger)

        while True:
            schedule.run_pending()
            time.sleep(1)
        

if __name__ == "__main__":
    print("TEST")
    tracker = Tracker()
    tracker.start(args[1])
