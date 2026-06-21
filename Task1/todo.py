# To-Do List Application

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

def view_tasks():
    print("\nTo-Do List:")
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def update_task(index, new_task):
    if 0 <= index < len(tasks):
        tasks[index] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid task number.")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Deleted: {removed}")
    else:
        print("Invalid task number.")

# Demo execution
add_task("Complete CODSOFT Task 1")
add_task("Practice Python")

view_tasks()

update_task(0, "Submit CODSOFT Task 1")

view_tasks()

delete_task(1)

view_tasks()
