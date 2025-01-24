import schedule
import threading
import time
from datetime import datetime
from cloud_utils import CloudUtils

class TaskScheduler:
    def __init__(self):
        self.tasks = {}
        self.cloud_utils = CloudUtils()
        self.scheduler_thread = threading.Thread(target=self.run_scheduler)
        self.scheduler_thread.daemon = True
        self.scheduler_thread.start()

    def add_task(self, task_name, run_time):
        if task_name in self.tasks:
            raise ValueError(f"Task '{task_name}' is already scheduled.")
        
        run_time_obj = datetime.strptime(run_time, '%Y-%m-%d %H:%M:%S')
        schedule_time = run_time_obj.strftime('%H:%M:%S')
        
        schedule.every().day.at(schedule_time).do(self.cloud_utils.execute_task, task_name)
        self.tasks[task_name] = run_time
        print(f"Scheduled task: {task_name} at {run_time}")

    def list_tasks(self):
        return [{'task_name': name, 'run_time': time} for name, time in self.tasks.items()]

    def run_scheduler(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
