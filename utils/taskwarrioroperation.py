import subprocess
import json

def run_command(command):
    command = f"yes | {command}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    #print(f"Running Command: {command}")  # Debug: Print the command
    #print(f"Command Output: {result.stdout.strip()}")  # Debug: Print the command output
    #print(f"Command Error: {result.stderr.strip()}")  # Debug: Print any error messages
    return result.stdout.strip()

def add_task(description, due=None, priority=None, project=None, tags=None):
    command = f"task add \"{description}\""
    if due:
        command += f" due:{due}"
    if priority:
        command += f" priority:{priority}"
    if project:
        command += f" project:{project}"
    if tags:
        for tag in tags:
            command += f" +{tag}"
    return run_command(command)

def list_tasks():
    command = "task export"
    output = run_command(command)
    return json.loads(output)

def modify_task(task_id, modifications):
    command = f"task {task_id} modify"
    for key, value in modifications.items():
        command += f" {key}:{value}"
    return run_command(command)

def delete_task(task_id):
    command = f"task {task_id} delete"
    return run_command(command)
