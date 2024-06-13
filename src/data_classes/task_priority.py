from enum import Enum
import flet as ft


class Priority(Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    REPEATING = "REPEATING"


def GetPriorityByValue(priority_value: str) -> Priority:
    switch = {
        "HIGH": Priority.HIGH,
        "MEDIUM": Priority.MEDIUM,
        "LOW": Priority.LOW,
        "REPEATING": Priority.REPEATING
    }
    return switch[priority_value]


class TaskPriority:
    def __init__(self, priority: Priority):
        self.task_priority: Priority = priority

    def get_color(self) -> str:
        switch = {
            Priority.HIGH: ft.colors.RED,
            Priority.MEDIUM: ft.colors.YELLOW,
            Priority.LOW: ft.colors.GREEN,
            Priority.REPEATING: ft.colors.BLUE
        }
        return switch[self.task_priority]

    def get_text(self) -> str:
        switch = {
            Priority.HIGH: "Высокий приоритет",
            Priority.MEDIUM: "Средний приоритет",
            Priority.LOW: "Низкий приоритет",
            Priority.REPEATING: "Повторяющаяся задача"
        }
        return switch[self.task_priority]

    def get_icon(self) -> str:
        if self.task_priority == Priority.REPEATING:
            return ft.icons.REPEAT
        return ft.icons.BOOKMARK

