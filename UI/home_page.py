import flet as ft
# import flet_core as ft_core
import ui.controls.task_control as task_control


class HomePage:
    today_tasks_text: ft.Text = ft.Text("Задачи на сегогндя", size=20)
    tomorrow_tasks_text: ft.Text = ft.Text("Задачи на завтра")
    add_task_button: ft.FloatingActionButton = ft.FloatingActionButton(icon=ft.icons.ADD)
    sort_button: ft.IconButton = ft.IconButton(icon=ft.icons.SORT, tooltip="Смена глобальной сортировки")

    t1 = task_control.TaskControl('asdfasdfasd')
    t2 = task_control.TaskControl('asdfasdkf;ja4564asdfsjasdkl;fj;asdklfj;asdklfjlasdkjfasdl;fjasdklfjkl;sdafj;lsdajfalkjfl;asdkfjasdkl;fjsdrtjioqwerutiojklfjasdkl;fjasdklfjasdkfndm,safnmsd,fasdjkjfaksd;fljdafsdafasdfasdf6546546545sd;fjasdjf')

    today_tasks_column: ft.Column = ft.Column([
        ft.Row([today_tasks_text, sort_button], spacing=20, alignment=ft.MainAxisAlignment.CENTER),
        t1.task_card,
        t2.task_card
    ])

    today_tasks_container: ft.Container = ft.Container(today_tasks_column, padding=ft.padding.only(top=15))

    controls: [ft.Control] = [
        today_tasks_container,
        add_task_button
    ]
