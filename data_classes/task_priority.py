from enum import Enum
import flet as ft


class Priority(Enum):
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    REPEATING = 0


class TaskPriority:
    def __init__(self, priority: Priority):
        self.task_priority = priority

    def get_color(self) -> ft.colors:
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

    def get_icon(self) -> ft.icons:
        if self.task_priority == Priority.REPEATING:
            return ft.icons.REPEAT
        return ft.icons.BOOKMARK

