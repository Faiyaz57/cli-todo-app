# cli-todo-app
i implement this code for to do list task and read me also added
 Project: CLI To-Do List App in Python
This is a terminal-based to-do list where users can:

View tasks

Add new tasks

Mark tasks as done

Delete tasks

Store tasks in a JSON file for persistence

🔍 Main Components of the Code
1. File Storage
All tasks are saved in a file called todo_list.json.

This allows the app to remember your tasks even after closing.

python
Copy
Edit
def load_tasks():   # Reads tasks from the file
def save_tasks():   # Saves updated task list back to the file
2. User Actions
Each user action is handled by a function:

Function Name	What It Does
view_tasks()	Displays the list of all tasks
add_task()	Lets user input a new task
mark_done()	Marks a selected task as "done ✅"
delete_task()	Deletes a task based on user choice

3. Main Menu (Loop)
The app keeps running until the user chooses to exit:

python
Copy
Edit
while True:
    print("1. View Tasks")
    print("2. Add Task")
    ...
Each menu option is linked to a corresponding function.

✅ Sample Flow
text
Copy
Edit
==== 🧾 TO-DO LIST APP ====
1. View Tasks
2. Add Task
3. Mark Task as Done
4. Delete Task
5. Exit
🧠 Extras
It uses standard Python libraries: os and json.

The use of emojis (✅ ❌ 🗑️) makes it user-friendly.

Tasks are stored as dictionaries like:

json
Copy
Edit
{"task": "Buy groceries", "done": false}
