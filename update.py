import json
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

def update_task_list():
    """Update the displayed tasks."""
    task_list.delete(*task_list.get_children())  # Clear treeview
    tasks = load_tasks()
    for task in tasks:
        status = "✔" if task["completed"] else "✖"
        task_list.insert("", "end", values=(task['id'], status, task['title'], task['description'], task['priority']))

