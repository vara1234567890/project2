import os

# Function to load tasks from a file
def load_tasks(filename="tasks.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = [task.strip() for task in file.readlines()]
        return tasks
    return []

# Function to save tasks to a file
def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")
    save_tasks(tasks)

def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        task = tasks.pop(task_num - 1)
        print(f"Task '{task}' deleted.")
        save_tasks(tasks)
    except (IndexError, ValueError):
        print("Invalid task number.")

def mark_task_complete(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to mark as complete: "))
        tasks[task_num - 1] += " (Completed)"
        print(f"Task {task_num} marked as complete.")
        save_tasks(tasks)
    except (IndexError, ValueError):
        print("Invalid task number.")

def task_manager():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_task_complete(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the task manager
task_manager()