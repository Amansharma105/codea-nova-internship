# Program: To-Do List Manager
# Developer: Aman
# Description: 
#   Simple To-Do List in Python.
#   Add multiple tasks, view tasks, delete tasks.
# Initialize empty To-Do list
todo_list = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task(s)")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        # Add one or multiple tasks
        tasks = input("Enter tasks separated by comma: ")
        task_list = [task.strip() for task in tasks.split(',') if task.strip()]
        if task_list:
            todo_list.extend(task_list)
            print(f"{len(task_list)} task(s) added successfully!")
        else:
            print("No valid tasks entered.")

    elif choice == '2':
        if not todo_list:
            print("Your To-Do List is empty.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")

    elif choice == '3':
        if not todo_list:
            print("Nothing to delete, list is empty.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(todo_list):
                    removed_task = todo_list.pop(task_num - 1)
                    print(f"Task '{removed_task}' deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '4':
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a number between 1-4.")