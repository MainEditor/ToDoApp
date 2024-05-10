import flet as ft
import datetime
import flet_core as ft_core


class TaskControl:
    def __init__(self,
                 # deadline: datetime.datetime,
                 # priority: int,
                 name: str,
                 # description: str,
                 # notification_datetime: datetime.datetime,
                 # repetition_interval: str):
                 ):
        self.task_name: ft.Container = ft.Container(ft.Text(name), expand=True)
        self.edit_button: ft.IconButton = ft.IconButton(icon=ft.icons.EDIT)
        self.delete_button: ft.IconButton = ft.IconButton(icon=ft.icons.DELETE, icon_color=ft.colors.RED_ACCENT)
        self.description_text: ft.Text = ft.Text()
        self.row: ft.Row = ft.Row([
            ft.Checkbox(),
            self.task_name,
            # self.task_name_text,
            ft.Column([self.delete_button,
                       self.edit_button], spacing=3)
        ], spacing=3)

        self.task_card: ft.Card = ft.Card(ft.Container(self.row, padding=3))
