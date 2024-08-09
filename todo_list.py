def display_tasks(tasks):
    if len(tasks) == 0:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks):
            status = "[Completed]" if task['completed'] else "[Not Completed]"
            print(f"{i + 1}. {task['name']} {status}")

def add_task(tasks):
    task_name = input("Enter the task name: ")
    tasks.append({'name': task_name, 'completed': False})
    print("Task added.")

def mark_task_completed(tasks):
    display_tasks(tasks)
    task_number = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]['completed'] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def remove_task(tasks):
    display_tasks(tasks)
    task_number = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)
        print("Task removed.")
    else:
        print("Invalid task number.")

def main():
    tasks = []

    while True:
        print("\nTo-Do List Application Instructions")
        print("1. Display To-Do List")
        print("2. Add a Task")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Quit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
