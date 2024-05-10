import flet as ft
import flet_core as ft_core


class HomePage:
    today_tasks_text: ft.Container = ft.Container(ft.Text("Задачи на сегогндя"),
                                                  margin=ft.margin.only(top=20), scale=1.44)
    tomorrow_tasks_text: ft.Text = ft.Text("Задачи на завтра")
    add_task_button: ft.FloatingActionButton = ft.FloatingActionButton(icon=ft.icons.ADD)

    today_tasks_column: ft.Column = ft.Column([
        today_tasks_text
    ])

    controls = [
        today_tasks_column,
        add_task_button
    ]
