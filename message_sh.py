import flet as ft


class Message(ft.Container):
    def __init__(self, author, body, time):
        super().__init__()
        self.content = ft.Column(
            controls=[
                ft.Text(time, color=ft.colors.BLACK),
                ft.Text(author, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                ft.Text(body,color=ft.colors.BLACK),
            ],
        )
        self.border = ft.border.all(1, ft.colors.BLACK)
        self.border_radius = ft.border_radius.all(10)
        self.bgcolor = ft.colors.GREEN_200
        self.padding = 10
        self.expand = True
        self.expand_loose = True