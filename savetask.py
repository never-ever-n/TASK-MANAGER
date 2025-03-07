import json
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


