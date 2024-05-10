import flet as ft
import flet_core as ft_core
import ui.home_page as home_ui

home = home_ui.HomePage()


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
        # on_change=on_change
    )

    page.scroll = ft.ScrollMode.ADAPTIVE

    page.add(*home.controls)


ft.app(target=main)
