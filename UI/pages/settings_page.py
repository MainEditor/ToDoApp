import flet as ft
from ui.controls import task_block
from ui.pages.home_page import HomePage
from data_classes.task_priority import Priority
from data_classes.task_block_mode_enum import TaskBlockMode


class SettingsPage:
    @staticmethod
    def change_theme(e: ft.ControlEvent):
        switch = {
            "DARK": ft.ThemeMode.DARK,
            "LIGHT": ft.ThemeMode.LIGHT,
            "SYSTEM": ft.ThemeMode.SYSTEM
        }

        e.page.theme_mode = switch[e.data]
        e.page.update()

    def change_task_layout(self, e: ft.ControlEvent):
        switch = {"MINIMAL": TaskBlockMode.COMPACT, "EXTENDED": TaskBlockMode.EXTENDED}

        for task in HomePage.tasks:
            task.change_mode(switch[e.data])

    def __init__(self, page):
        self.page = page

        select_theme_text: ft.Row = ft.Row(controls=[ft.Icon("CONTRAST"), ft.Text("Тема приложения:", size=17)])
        theme_selector: ft.RadioGroup = ft.RadioGroup(content=ft.Column([
            ft.Row(controls=[ft.Radio(value="DARK", label="Тёмная"), ft.Icon(name="DARK_MODE")]),
            ft.Row(controls=[ft.Radio(value="LIGHT", label="Светлая"), ft.Icon(name="LIGHT_MODE")]),
            ft.Row(controls=[ft.Radio(value="SYSTEM", label="Системная"), ft.Icon(name="ANDROID")])
        ]),
            on_change=self.change_theme, value="SYSTEM")

        theme_settings_column: ft.Column = ft.Column([
            select_theme_text,
            theme_selector
        ])
        theme_settings_container: ft.Container = ft.Container(theme_settings_column, padding=ft.padding.only(top=30))

        minimal_block = task_block.EmptyTaskBlock()
        minimal_block.change_mode(TaskBlockMode.COMPACT)

        extended_block = task_block.EmptyTaskBlock()

        mode_selector: ft.RadioGroup = ft.RadioGroup(content=ft.Column(controls=[
            ft.Row(controls=[ft.Radio(value="MINIMAL"), minimal_block]),
            ft.Row(controls=[ft.Radio(value="EXTENDED"), extended_block]),
        ]), on_change=self.change_task_layout, value="EXTENDED")

        theme_settings_column: ft.Column = ft.Column([ft.Text("Макет заадчи:", size=17), mode_selector])

        mode_container: ft.Container = ft.Container(theme_settings_column)

        self.controls: [ft.Control] = [
            theme_settings_container,
            ft.Divider(),
            mode_container
        ]
