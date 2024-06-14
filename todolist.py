import tkinter as tk
from tkinter import messagebox

# Function to add a task to the to-do list
def add_task():
    task = task_entry.get()
    if task:
        todo_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_list()

# Function to remove a task from the to-do list
def remove_task():
    try:
        index = todo_listbox.curselection()[0]
        todo_listbox.delete(index)
        save_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Function to save the to-do list to a file
def save_list():
    with open("todo.txt", "w") as f:
        tasks = todo_listbox.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

# Function to load the to-do list from a file
def load_list():
    if not os.path.exists("todo.txt"):
        return
    with open("todo.txt", "r") as f:
        for line in f:
            todo_listbox.insert(tk.END, line.strip())

# Create the main tkinter window
root = tk.Tk()
root.title("To-Do List")

# Create and place widgets
task_entry = tk.Entry(root, width=50)
task_entry.grid(row=0, column=0, padx=5, pady=5)

add_button = tk.Button(root, text="Add Task", width=10, command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=5)

remove_button = tk.Button(root, text="Remove Task", width=10, command=remove_task)
remove_button.grid(row=1, column=1, padx=5, pady=5)

todo_listbox = tk.Listbox(root, height=15, width=60)
todo_listbox.grid(row=1, column=0, padx=5, pady=5)

# Load existing to-do list from file (if any)
load_list()

# Run the tkinter main loop
root.mainloop()
