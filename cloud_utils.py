class CloudUtils:
    def execute_task(self, task_name):
        print(f"Executing task: {task_name}")
        return f"Task '{task_name}' executed successfully on the cloud."

    def stop_task(self, task_name):
        print(f"Stopping task: {task_name}")
        return f"Task '{task_name}' stopped successfully on the cloud."
