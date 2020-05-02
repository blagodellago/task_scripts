#!/usr/bin/python3
# blago
# 5/1/20
from datetime import *

class Task:
# Task(<type of task>, <priority>, <date due>)
    def __init__(self, task, priority, due, date_added=datetime.now()):
        self.task = task
        self.priority = priority
        self.due = datetime.strptime(due, "%m-%d-%y")
        self.date_added = date_added
        with open('/Users/blakeedmond/Desktop/python_scripts/tasks.txt', 'a') as f:
            f.write(repr(self) + "\n")

    def __repr__(self):
        return f"{self.task} | priority: {self.priority} | due: {self.due}"


