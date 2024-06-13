import select
import flet as ft
from ui.pages import calendar_page, home_page, settings_page


def main(page: ft.Page):
    # page.client_storage.clear()
    print(page.client_storage.get("Tasks"))

    # page.client_storage.clear()
    def getTasks():
        if page.client_storage.contains_key("Tasks"):
            return page.client_storage.get("Tasks")
        return []

    home: home_page.HomePage = home_page.HomePage(page, getTasks())
    settings: settings_page.SettingsPage = settings_page.SettingsPage(page)

    def on_change(e: ft.ControlEvent):
        switch = {
            "0": settings.controls,
            "1": home.controls
            # "2":
        }
        home_page.update_tasks(getTasks(), e)
        e.page.controls = switch[e.data]
        print(home.controls)
        e.page.update()
    
    # page.bullshit = 3
    # page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD, text="Добавить задачу")

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
        on_change=on_change, selected_index=1
    )

    page.scroll = ft.ScrollMode.HIDDEN
    # page.floating_action_button_location = ft.FloatingActionButtonLocation.
    # page.theme_mode = ft.ThemeMode.LIGHT

    # page.controls = home.controls
    page.controls = home.controls
    page.update()


if __name__ == "__main__":
    ft.app(target=main)

