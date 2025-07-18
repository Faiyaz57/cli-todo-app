import os
import json

FILE_NAME = "todo_list.json"

# Load existing tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# View all tasks (new dedicated function)
def view_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found!")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {status} {task['task']}")
    print()

# Add a new task
def add_task(tasks):
    task_text = input("Enter the task: ").strip()
    if task_text:
        tasks.append({"task": task_text, "done": False})
        save_tasks(tasks)
        print("✅ Task added!\n")
    else:
        print("❗ Task cannot be empty.\n")

# Mark a task as done
def mark_done(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as done: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            save_tasks(tasks)
            print("🎉 Task marked as done!\n")
        else:
            print("❗ Invalid task number.\n")
    except ValueError:
        print("❗ Please enter a valid number.\n")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed['task']}' deleted!\n")
        else:
            print("❗ Invalid task number.\n")
    except ValueError:
        print("❗ Please enter a valid number.\n")

# Main CLI loop
def main():
    tasks = load_tasks()
    while True:
        print("==== 🧾 TO-DO LIST APP ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
