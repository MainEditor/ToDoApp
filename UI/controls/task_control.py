import flet as ft
import datetime
import flet_core as ft_core


class TaskControl:
    container: ft.Row = ft.Row()

    def __init__(self,
                 deadline: datetime.datetime,
                 priority: int,
                 name: str,
                 description: str,
                 notification_datetime: datetime.datetime,
                 repetition_interval: str):
        self.container.controls = [ft.Text(name)]
