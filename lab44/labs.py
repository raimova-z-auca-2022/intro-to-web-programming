import tkinter as tk
from tkinter import simpledialog
import json
import os


filename = "tasks.json"

def load_tasks():
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

def save_tasks():
    with open(filename, "w") as f:
        json.dump(tasks, f)

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append({"text": task, "completed": False})
        entry.delete(0, tk.END)
        save_tasks()
        render_tasks()

def toggle_complete(index):
    tasks[index]["completed"] = not tasks[index]["completed"]
    save_tasks()
    render_tasks()

def delete_task(index):
    del tasks[index]
    save_tasks()
    render_tasks()

def edit_task(index):
    new_text = simpledialog.askstring("Edit Task", "Update the task:", initialvalue=tasks[index]["text"])
    if new_text:
        tasks[index]["text"] = new_text.strip()
        save_tasks()
        render_tasks()

def render_tasks(i=None):
    for widget in list_frame.winfo_children():
        widget.destroy()
    for i, task in enumerate(tasks):
        text = task["text"]
        label = tk.Label(list_frame, text=text, width=40, anchor="w")
        if task["completed"]:
            label.config(fg="gray", font=("Arial", 10, "overstrike"))
        else:
            label.config(fg="black", font=("Arial", 10))
        label.grid(row=i, column=0, padx=5, pady=2)

        btn_complete = tk.Button(list_frame, text="✔", command=lambda i=i: toggle_complete(i))
        btn_complete.grid(row=i, column=1)

        btn_edit = tk.Button(list_frame, text="✏", command=lambda i=i: edit_task(i))
        btn_edit.grid(row=i, column=2)

        btn_delete = tk.Button(list_frame, text="✖", command=lambda i=i: delete_task(i))
        btn_delete.grid(row=i, column=3)

tasks = load_tasks()

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

btn_add = tk.Button(root, text="Add Task", command=add_task)
btn_add.pack()

list_frame = tk.Frame(root)
list_frame.pack(pady=10)

render_tasks()

root.mainloop()
