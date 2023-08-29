import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", " Please enter a task to add .")

# Function to remove a selected task
def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Function to view tasks
def view_tasks():
    tasks = listbox.get(0, tk.END)
    if tasks:
        tasks_str = "\n".join(tasks)
        messagebox.showinfo("To-Do List", "All Tasks : \n" + tasks_str)
    else:
        messagebox.showinfo("To-Do List", "No tasks in the list.")

# Function to update a selected task
def update_task():
    try:
        selected_task_index = listbox.curselection()[0]
        current_task = listbox.get(selected_task_index)
        new_task = entry.get()
        if new_task:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, new_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a new task details.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Create the main window
root = tk.Tk()
root.title(" To-Do List ")

# Entry widget for adding tasks
entry = tk.Entry(root, width=30)
entry.pack(pady=15)

# Add task button
add_butn = tk.Button(root, text="Add Task", command = add_task)
add_butn.pack()

# Remove task button
remove_butn = tk.Button(root, text="Remove Task", command = remove_task)
remove_butn.pack()

# Edit task button
update_butn = tk.Button(root, text="Update Task", command = update_task)
update_butn.pack()

# View tasks button
view_butn = tk.Button(root, text="View Tasks", command = view_tasks)
view_butn.pack()

# Listbox to display tasks
listbox = tk.Listbox(root, width=40)
listbox.pack()

# Function to center the window on the screen
def center_window(width=400, height=300):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

# Center the main window
center_window(400, 400)

# Start the Tkinter main loop
root.mainloop()
