from datetime import datetime
from task_manager.validation import validate_task_title (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Import validation functions
#None

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    try:
        # Validate inputs
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Create task dictionary
    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    #None
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    try:
        # Validate index
        if not isinstance(index, int):
            raise ValueError("Index must be a number.")

        if index < 0 or index >= len(tasks):
            raise IndexError("Invalid task index.")

        tasks[index]["completed"] = True
    #None
    print("Task marked as complete!")
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")


    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
      print("\n--- Pending Tasks ---")
    pending_found = False

    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"{i}. {task['title']} (Due: {task['due_date']})")
            pending_found = True

    if not pending_found:
        print("No pending tasks.")
    #None

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return 0

    completed_tasks = sum(1 for task in tasks if task["completed"])
    progress = (completed_tasks / len(tasks)) * 100

    print(f"Progress: {completed_tasks}/{len(tasks)} tasks completed ({progress:.2f}%)")
    
    #None
    return progress