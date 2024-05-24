import pytest
import utils.taskwarrioroperation as taskwarrioroperation
import random

# Add a new task
def test_add_task():
    result = taskwarrioroperation.add_task("Test task", due="2024-06-01", priority="H", project="TestProject", tags=["test"])
    #print("result1"+f"{result}")
    assert "Created task" in result

# List down all avaialble task
def test_list_tasks():
    tasks = taskwarrioroperation.list_tasks()
    assert isinstance(tasks, list)

# Modify an existing task by id
def test_modify_task():
    tasks = taskwarrioroperation.list_tasks()
    if tasks:
       # task_id = tasks[0]["id"]  there are multiple task with id 0 in database hence hardcoded with id 1 
        task_id = 1
        random_number = random.randint(10, 99)
        tagvalue = "test"+f"{random_number}"
        result = taskwarrioroperation.modify_task(task_id, {"tags": tagvalue})
        assert "Modified 1 task" in result
#Delete a task by id
def test_delete_task():
    tasks = taskwarrioroperation.list_tasks()
    if tasks:
        # task_id = tasks[0]["id"]
        task_id = 1
        result = taskwarrioroperation.delete_task(task_id)
        assert "Deleted 1 task" in result
