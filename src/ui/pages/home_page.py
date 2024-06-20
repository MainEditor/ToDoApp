import flet as ft
from data_classes.sort_enum import SortType
from ui.controls.task_block import TaskBlock, InvisibleTaskBlock
from ui.pages.task_settings_page import TaskSettingsPage
from data_classes.task_priority import GetPriorityByValue
from ui.controls.task_block import TaskBlock
from data_classes.task import Task
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

def update_tasks(tasks: List[Task], e: ft.Page):
    HomePage.tasks = [TaskBlock(Task(GetPriorityByValue(task["priority"]), task["task_text"])) for task in tasks] if len(tasks) > 0 else [ft.Text("Пусто!")]

    today_tasks_column = ft.Column([
        ft.Row([HomePage.today_tasks_text, HomePage.sort_button], spacing=20, alignment=ft.MainAxisAlignment.CENTER),
        *HomePage.tasks,
        InvisibleTaskBlock()
    ])

    today_tasks_container = ft.Container(today_tasks_column, padding=ft.padding.only(top=25))
    HomePage.controls = [today_tasks_container, HomePage.add_task_floating_button]
    e.page.controls = HomePage.controls
    e.page.update()

def add_task(e: ft.ControlEvent):
    print("Открыт экран добавления задачи")
    e.page.controls = TaskSettingsPage.controls
    e.page.update()


class HomePage:
    sorted_by_priority: SortType = SortType.BY_PRIORITY
    
    sort_button: ft.OutlinedButton = ft.OutlinedButton(content=ft.Icon(name="SORT"), tooltip="Смена глобальной сортировки", on_click=sort_tasks)
    today_tasks_text: ft.Text = ft.Text("Задачи на сегодня", size=20)
    tomorrow_tasks_text: ft.Text = ft.Text("Задачи на завтра")
    add_task_floating_button: ft.FloatingActionButton = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_task)

    tasks: List[TaskBlock] = []
    controls: List[ft.Control] = []

    def __init__(self, page: ft.Page, tasks: List[Task]):
        self.page = page
        

        self.task_settings_page: TaskSettingsPage = TaskSettingsPage(page)
        # page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_FLOAT
        self.tasks = [TaskBlock(Task(GetPriorityByValue(task["priority"]), task["task_text"])) for task in tasks] if len(tasks) > 0 else [ft.Text("Пусто!")]

        today_tasks_column: ft.Column = ft.Column([
        ft.Row([self.today_tasks_text, self.sort_button], spacing=20, 
               alignment=ft.MainAxisAlignment.CENTER
               ),
               *self.tasks,
               InvisibleTaskBlock()
        ])
        today_tasks_container: ft.Container = ft.Container(today_tasks_column, padding=ft.padding.only(top=25))
        
        self.controls: List[ft.Control] = [today_tasks_container, self.add_task_floating_button]