import flet as ft
from data_classes.sort_enum import SortType
from ui.controls.task_block import TaskBlock, InvisibleTaskBlock
from data_classes.task_priority import Priority
from typing import List

# def get_key():
#     if HomePage.sorted_by_priority == SortType.BY_PRIORITY:
#         return 
#     elif HomePage.sorted_by_priority == SortType.BY_DEADLINE:
#         return pass
    

def sort_tasks(e: ft.ControlEvent):
    HomePage.tasks = sorted(HomePage.tasks, key=lambda task: task.priority.task_priority.value, reverse=True)
    
    HomePage.today_tasks_column = ft.Column([
        ft.Row([HomePage.today_tasks_text, HomePage.sort_button], spacing=20, alignment=ft.MainAxisAlignment.CENTER),
        *HomePage.tasks,
        InvisibleTaskBlock()
    ])

    today_tasks_container: ft.Container = ft.Container(HomePage.today_tasks_column, padding=ft.padding.only(top=20))

    HomePage.controls = [
        today_tasks_container,
    ]
    
    e.page.controls = HomePage.controls
    e.page.update()


class HomePage:
    sorted_by_priority: SortType = SortType.BY_PRIORITY
    
    tasks: List[TaskBlock] = [TaskBlock(Priority.MEDIUM, "Дописать ТЗ проекта по проектному практикуму."),
                              TaskBlock(Priority.HIGH, "Доделать приложение."),
                              TaskBlock(Priority.LOW, "Посетить созвон с куратором."),
                              TaskBlock(Priority.MEDIUM, "Посетить онлайн пару."),
                              TaskBlock(Priority.HIGH, "Поработать на онлайн курсе."),
                              TaskBlock(Priority.REPEATING, "Записаться на предзащиту по проектному практикуму.")]
    
    sort_button: ft.OutlinedButton = ft.OutlinedButton(content=ft.Icon(name="SORT"), tooltip="Смена глобальной сортировки", on_click=sort_tasks)
    today_tasks_text: ft.Text = ft.Text("Задачи на сегогндя", size=20)
    tomorrow_tasks_text: ft.Text = ft.Text("Задачи на завтра")
    
    today_tasks_column: ft.Column = ft.Column([
        ft.Row([today_tasks_text, sort_button], spacing=20, alignment=ft.MainAxisAlignment.CENTER),
        *tasks,
        InvisibleTaskBlock()
    ])
    
    today_tasks_container: ft.Container = ft.Container(today_tasks_column, padding=ft.padding.only(top=20))
    
    controls: List[ft.Control] = [today_tasks_container]

    def __init__(self, page: ft.Page):
        self.page = page
