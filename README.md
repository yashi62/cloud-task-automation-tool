# Cloud Task Automation Tool

A Python-based tool for scheduling and automating tasks on cloud platforms.

## Features
- **Task Scheduling**: Schedule tasks to run at specific times.
- **Immediate Execution**: Trigger tasks to run immediately.
- **Cloud Interaction**: Simulate cloud task execution (e.g., AWS, Azure).
- **Task Listing**: Retrieve a list of all scheduled tasks.

## Setup

### Prerequisites
- Python 3.8 or higher

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cloud-task-automation.git
   cd cloud-task-automation
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask server:
   ```bash
   python app.py
   ```

### API Endpoints
1. **Schedule a Task**:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"task_name": "backup", "run_time": "2025-01-25 14:00:00"}' http://127.0.0.1:5000/schedule_task
   ```

2. **Execute a Task Immediately**:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"task_name": "backup"}' http://127.0.0.1:5000/execute_now
   ```

3. **List Scheduled Tasks**:
   ```bash
   curl http://127.0.0.1:5000/list_tasks
   ```

## License
MIT
