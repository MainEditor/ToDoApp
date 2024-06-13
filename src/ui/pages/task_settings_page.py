from typing import List
import flet as ft
from data_classes.task_priority import Priority, GetPriorityByValue
from ui.controls.task_block import TaskBlock
from data_classes.task import Task
import datetime
from ui.pages import home_page

def select_date(e: ft.ControlEvent):
    TaskSettingsPage.date_picker.pick_date()

def select_time(e: ft.ControlEvent):
    TaskSettingsPage.time_picker.pick_time()



def change_date(e: ft.ControlEvent):
    # print(f"Date picker changed, value is {TaskSettingsPage.date_picker.value}")
    ...


def change_time(e: ft.ControlEvent):
    ...

def save_and_write_task(e: ft.ControlEvent):

    print("ЗАДАЧА ДОБАВЛЕНА")

    if TaskSettingsPage.priority_selector.value == None or TaskSettingsPage.task_text_input.value == "":
        e.page.snack_bar = ft.SnackBar(content=ft.Row([ft.Icon(ft.icons.WARNING, color=ft.colors.RED), ft.Text("Укажите приоритет и/или введите текст!")]))
        e.page.snack_bar.open = True
        e.page.update()
        return
    
    if e.page.client_storage.contains_key("Tasks"):
        updated_tasks = e.page.client_storage.get("Tasks")
        updated_tasks += [Task(priority=GetPriorityByValue(TaskSettingsPage.priority_selector.value),
                                    task_text=TaskSettingsPage.task_text_input.value)]
        e.page.client_storage.set("Tasks", updated_tasks)
        home_page.update_tasks(tasks=e.page.client_storage.get("Tasks"), e=e)
        e.page.update()
        return

    created_tasks = [Task(priority=GetPriorityByValue(TaskSettingsPage.priority_selector.value),
                               task_text=TaskSettingsPage.task_text_input.value)]
    
    e.page.client_storage.set("Tasks", created_tasks)
    home_page.update_tasks(tasks=e.page.client_storage.get("Tasks"), e=e)

    # e.page.client_storage.set("Tasks", updated_tasks)


class TaskSettingsPage:
    page: ft.Page

    task_text_input: ft.TextField = ft.TextField(label="Текст вашей задачи")

    priority_selector: ft.RadioGroup = ft.RadioGroup(content=ft.Column(controls=[
            ft.Row(controls=[ft.Radio(value=Priority.HIGH.value), ft.Text("Высокий"), ft.Icon(color="RED", name=ft.icons.BOOKMARK)]),
            ft.Row(controls=[ft.Radio(value=Priority.MEDIUM.value), ft.Text("Средний"), ft.Icon(color="YELLOW", name=ft.icons.BOOKMARK)]),
            ft.Row(controls=[ft.Radio(value=Priority.LOW.value), ft.Text("Низкий"), ft.Icon(color="GREEN", name=ft.icons.BOOKMARK)]),
            ft.Row(controls=[ft.Radio(value=Priority.REPEATING.value), ft.Text("Повторяющийся"), ft.Icon(color="BLUE", name=ft.icons.REPEAT)])
            ]
        )
    )
    
    priority_selector_column: ft.Column = ft.Column(controls=[
        ft.Text("Приоритет"),
        priority_selector
    ])

    date_picker = ft.DatePicker(
        cancel_text="Отмена",
        confirm_text="Выбрать",
        help_text="Выберите дату",
        on_change=change_date,
        # on_dismiss=date_picker_dismissed,
        last_date=datetime.datetime.max,
    )

    time_picker = ft.TimePicker(
        confirm_text="Выбрать",
        cancel_text="Отмена",
        error_invalid_text="Ошибка",
        help_text="Выберите время",
        on_change=change_time,
        # on_dismiss=dismissed,
    )

    date_button = ft.ElevatedButton("Выбор даты", icon=ft.icons.CALENDAR_MONTH, on_click=select_date)


    time_button = ft.ElevatedButton("Выбор времени", icon=ft.icons.TIMER, on_click=select_time)

    date_time_row: ft.Row = ft.Row(controls=[date_button, time_button])

    add_task_button: ft.ElevatedButton = ft.ElevatedButton(text="Сохранить", scale=1.3, icon=ft.icons.SAVE, on_click=save_and_write_task)

    main_column: ft.Column = ft.Column(controls=[task_text_input, 
                                                 priority_selector_column,
                                                 date_time_row,
                                                 add_task_button,
                                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=35)
    main_container: ft.Container = ft.Container(main_column, padding=ft.padding.only(top=25))
    controls: List[ft.Control] = [main_container]

    def __init__(self, page: ft.Page) -> None:
        self.page: ft.Page = page
        page.overlay.append(self.date_picker)
        page.overlay.append(self.time_picker)
        # self.page.overlay.append(self.date_selector))