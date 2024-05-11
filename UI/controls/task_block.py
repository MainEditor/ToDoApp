import flet as ft
import datetime
# import flet_core as ft_core
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
        self.priority_mark: ft.Icon = ft.Icon(ft.icons.BOOKMARK, tooltip="Приоритет задачи",
                                              color=self.priority.get_color(),
                                              scale=1.1)
        self.check_box: ft.Checkbox = ft.Checkbox(scale=1.1)

        self.left_column: ft.Column = ft.Column([self.priority_mark, self.check_box],
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        self.task_text: ft.Container = ft.Container(ft.Text(task_text, size=18), expand=True)
        self.right_column: ft.Column = ft.Column([self.delete_button, self.edit_button], spacing=0)

        self.row: ft.Row = ft.Row([self.left_column, self.task_text, self.right_column], spacing=0)

        super().__init__(ft.Container(self.row, padding=3))


class InvisibleTaskBlock(TaskBlock):
    def __init__(self):
        super().__init__(Priority.LOW, str())
        self.opacity = 0

