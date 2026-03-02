from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str):
        raise ValueError("Title must be a string.")
    
    if title.strip() == "":
        raise ValueError("Title cannot be empty.")
    
    if len(title.strip()) < 3:
        raise ValueError("Title must be at least 3 characters long.")
    
    return True
    #None
    
def validate_task_description(description):
    if not isinstance(description, str):
        raise ValueError("Description must be a string.")
    
    if description.strip() == "":
        raise ValueError("Description cannot be empty.")
    
    return True
    #None    
    
def validate_due_date(due_date):
     if not isinstance(due_date, str):
        raise ValueError("Due date must be a string.")
    
    if due_date.strip() == "":
        raise ValueError("Due date cannot be empty.")
    
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")
    
    return True
    #None