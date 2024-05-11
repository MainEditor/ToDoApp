import flet as ft
# import flet_core as ft_core
# import ui.controls.task_block as task_block
from ui.controls.task_block import TaskBlock, InvisibleTaskBlock
from data_classes.task_priority import Priority


class HomePage:
    today_tasks_text: ft.Text = ft.Text("Задачи на сегогндя", size=20)
    tomorrow_tasks_text: ft.Text = ft.Text("Задачи на завтра")
    add_task_button: ft.FloatingActionButton = ft.FloatingActionButton(icon=ft.icons.ADD, text="Добавить задачу")
    sort_button: ft.IconButton = ft.IconButton(icon=ft.icons.SORT, tooltip="Смена глобальной сортировки")

    # t1 = TaskBlock(Priority.HIGH, 'Сделать что-то очень важное')
    # t2 = TaskBlock(Priority.REPEATING, 'Сделать ещё что-то очень важное')

    today_tasks_column: ft.Column = ft.Column([
        ft.Row([today_tasks_text, sort_button], spacing=20, alignment=ft.MainAxisAlignment.CENTER),
        *[TaskBlock(Priority.MEDIUM, str(i)) for i in range(10)],
    ])

    today_tasks_column.controls += [InvisibleTaskBlock()]

    today_tasks_container: ft.Container = ft.Container(today_tasks_column, padding=ft.padding.only(top=20))

    controls: [ft.Control] = [
        today_tasks_container,
        add_task_button
    ]
