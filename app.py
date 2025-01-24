from flask import Flask, request, jsonify
from task_scheduler import TaskScheduler
from cloud_utils import CloudUtils

app = Flask(__name__)
scheduler = TaskScheduler()
cloud_utils = CloudUtils()

@app.route('/schedule_task', methods=['POST'])
def schedule_task():
    data = request.json
    task_name = data.get('task_name')
    run_time = data.get('run_time')  # Format: 'YYYY-MM-DD HH:MM:SS'

    if not task_name or not run_time:
        return jsonify({'error': 'Both task_name and run_time are required'}), 400

    try:
        scheduler.add_task(task_name, run_time)
        return jsonify({'message': f'Task "{task_name}" scheduled for {run_time}.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/execute_now', methods=['POST'])
def execute_now():
    data = request.json
    task_name = data.get('task_name')

    if not task_name:
        return jsonify({'error': 'Task name is required'}), 400

    try:
        response = cloud_utils.execute_task(task_name)
        return jsonify({'message': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/list_tasks', methods=['GET'])
def list_tasks():
    tasks = scheduler.list_tasks()
    return jsonify({'tasks': tasks}), 200


if __name__ == "__main__":
    app.run(debug=True)
