import json
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

def delete_task():
    """Delete selected task."""
    selected_item = task_list.selection()
    if not selected_item:
        messagebox.showerror("Error", "No task selected!")
        return

    task_id = task_list.item(selected_item, "values")[0]
    tasks = load_tasks()
    tasks = [task for task in tasks if str(task["id"]) != task_id]
    save_tasks(tasks)
    update_task_list()