import flet as ft
from ui.pages import calendar_page, home_page, settings_page, task_parameters_page

home = home_page.HomePage()
settings = settings_page.SettingsPage()

def on_change(e: ft.ControlEvent):
    swtich = {
        "0": settings.controls,
        "1": home.controls
        # "2":
    }
    e.page.controls = swtich[e.data]
    e.page.update()


def main(page: ft.Page):
    page.title = "ToDo"
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.SETTINGS_OUTLINED, selected_icon=ft.icons.SETTINGS,
                                     label="Настройки"),
            ft.NavigationDestination(icon=ft.icons.HOME_OUTLINED, selected_icon=ft.icons.HOME_ROUNDED,
                                     label="Дом"),
            ft.NavigationDestination(icon=ft.icons.CALENDAR_MONTH_OUTLINED,
                                     selected_icon=ft.icons.CALENDAR_MONTH,
                                     label="Календарь")
        ],
        on_change=on_change, border=ft.Border(top=ft.BorderSide(width=0))
    )

    page.scroll = ft.ScrollMode.HIDDEN
    # page.floating_action_button_location = ft.FloatingActionButtonLocation.
    # page.theme_mode = ft.ThemeMode.LIGHT

    page.add(*settings.controls)


if __name__ == "__main__":
    ft.app(target=main)
