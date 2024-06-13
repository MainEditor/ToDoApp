from data_classes.task_priority import Priority
from datetime import datetime

class Task:
    def __init__(self, priority: Priority, task_text: str) -> None:
        self.priority = priority
        self.task_text = task_text
        # self.creation_date_ID = str(datetime.now.) TODO: сделать ID