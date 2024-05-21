import flet as ft
from typing import Any
import datetime
from data_classes.task_block_mode_enum import TaskBlockMode
from data_classes.task_priority import Priority, TaskPriority


class TaskBlock(ft.Card):
    def __init__(self,
                 # deadline: datetime.datetime,
                 priority: Priority,
                 task_text: str,
                 # notification_datetime: datetime.datetime,
                 # repetition_interval: str):
                ):
        self.priority: TaskPriority = TaskPriority(priority)

        self.edit_button: ft.IconButton = ft.IconButton(icon=ft.icons.EDIT)
        self.delete_button: ft.IconButton = ft.IconButton(icon=ft.icons.DELETE, icon_color=ft.colors.RED_ACCENT)
        self.description_text: ft.Text = ft.Text()
        self.priority_mark: ft.Icon = ft.Icon(name=self.priority.get_icon(), tooltip=self.priority.get_text(),
                                              color=self.priority.get_color())
        self.check_box: ft.Checkbox = ft.Checkbox()

        self.left_column: ft.Column = ft.Column([self.priority_mark, self.check_box],
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        self.task_text: ft.Container = ft.Container(ft.Text(task_text, size=18), expand=True)
        self.right_column: ft.Column = ft.Column([self.delete_button, self.edit_button], spacing=0)

        self.row: ft.Row = ft.Row([self.left_column, self.task_text, self.right_column], spacing=0)

        super().__init__(ft.Container(self.row, padding=3))

    def change_mode(self, change_to: TaskBlockMode):
        if change_to == TaskBlockMode.EXTENDED:
            self.row: ft.Row = ft.Row([self.left_column, self.task_text, self.right_column], spacing=0)
        elif change_to == TaskBlockMode.COMPACT:
            self.row: ft.Row = ft.Row([self.left_column, self.task_text], spacing=0)

        self.content = ft.Container(self.row, padding=3)


class InvisibleTaskBlock(TaskBlock):
    def __init__(self):
        super().__init__(Priority.LOW, str())
        self.opacity = 0


class TranslucentTaskBlock(TaskBlock):
    def __init__(self):
        super().__init__(Priority.LOW, "Текст вашей задачи")
        self.delete_button.opacity = self.priority_mark.opacity = self.opacity = 0.7
        self.disabled = True
        self.check_box.value = True
        self.task_text.expand = False
        self.expand = True
