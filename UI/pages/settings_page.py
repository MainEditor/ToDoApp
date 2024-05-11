import flet as ft


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

    select_theme_text: ft.Text = ft.Text("Тема приложения:", size=17)
    theme_selector: ft.RadioGroup = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="DARK", label="Тёмная"),
        ft.Radio(value="LIGHT", label="Светлая"),
        ft.Radio(value="SYSTEM", label="Системная")]),
        on_change=change_theme, value="SYSTEM")

    settings_column: ft.Column = ft.Column([
        select_theme_text,
        theme_selector
    ])
    settings_container: ft.Container = ft.Container(settings_column, padding=ft.padding.only(top=20))

    controls: [ft.Control] = [
        settings_container
    ]
