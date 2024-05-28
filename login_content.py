import sqlite3
import counter
import flet as ft
import datetime
from dd_delete_table import clean_massage_base
import navbar
import nav_content_corce
import random
from message_sh import Message
import asyncio
from message_cls import message_broker



class Constructor(ft.AppBar, ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.asyncio = asyncio
        self.f = ft.Text("Введите код-пароль", size=20)
        self.ki = []
        self.row_stars = ft.Row(alignment=ft.MainAxisAlignment.CENTER)
        self.text = ft.Text("Регистрация")
        self.text1 = ft.Text("Авторизация")
        self.text3 = ft.Text("Упрощенная авторизация")
        self.user_login = ft.TextField(label="Логин", width=300, on_change=self.validate)
        self.user_pass = ft.TextField(label="Пароль", password=True, width=300, on_change=self.validate)
        self.user_short_pass = ft.TextField(label="Ведите короткий пароль (5 цифр)", password=True, width=300,
                                       on_change=self.validate)
        self.button_reg = ft.OutlinedButton("Регистрация", width=200, on_click=self.registration, disabled=True)
        self.button_aus = ft.OutlinedButton("Авторизация", width=200, on_click=self.auth_users)
        self.button_back = ft.OutlinedButton("Назад", width=200, on_click=self.crete_home_content)
        self.button_back_reg_panel = ft.OutlinedButton("Выйти", width=200, on_click=self.create_start_panel)
        self.button_short_aus = ft.OutlinedButton("Авторизация", width=200, on_click=self.short_uth_users, disabled=True)
        self.button_corse = ft.OutlinedButton("Установить курсы", width=200, url="/corse/")
        self.button_clean = ft.OutlinedButton("Очистить", width=200, on_click=self.clean_messages)

        self.button_style = ft.ButtonStyle(
            shape=ft.CircleBorder(),
            padding=20

        )

        self.button_text_size = 30

        self.short_auth_panel = ft.Column(
            [
                ft.Row(
                    [
                        ft.ElevatedButton(
                            content=ft.Text("1", size=self.button_text_size),
                            on_click=self.on_button_click,
                            style=self.button_style,
                            expand=True,
                        ),
                        ft.ElevatedButton(
                            content=ft.Text("2", size=self.button_text_size),
                            on_click=self.on_button_click,
                            style=self.button_style,
                            expand=True,
                        ),
                        ft.ElevatedButton(
                            content=ft.Text("3", size=self.button_text_size),
                            on_click=self.on_button_click,
                            style=self.button_style,
                            expand=True,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
                ft.Row(
                    [
                        ft.ElevatedButton(
                            content=ft.Text("4", size=self.button_text_size),
                            on_click=self.on_button_click,
                            style=self.button_style,
                            expand=True,
                        ),
                        ft.ElevatedButton(
                            content=ft.Text("5", size=self.button_text_size),
                            on_click=self.on_button_click,
                            style=self.button_style,
                            expand=True,
                        ),
                        ft.ElevatedButton(
                            content=ft.Text("6", size=self.button_text_size),
                            on_click=self.on_button_click,
                            style=self.button_style,
                            expand=True,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
                ft.Row(
                    [
                        ft.ElevatedButton(
                            content=ft.Text("7", size=self.button_text_size),
                            on_click=self.on_button_click,
                            style=self.button_style,
                            expand=True,
                        ),
                        ft.ElevatedButton(
                            content=ft.Text("8", size=self.button_text_size),
                            on_click=self.on_button_click,
                            style=self.button_style,
                            expand=True,
                        ),
                        ft.ElevatedButton(
                            content=ft.Text("9", size=self.button_text_size),
                            on_click=self.on_button_click,
                            style=self.button_style,
                            expand=True,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
                ft.Row(
                    [
                        ft.ElevatedButton(
                            content=ft.Text("0", size=self.button_text_size),
                            on_click=self.on_button_click,
                            style=self.button_style,
                            expand=True,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )


    #     self.short_auth_panel = ft.Column(
    #     [
    #         ft.Row(
    #             [
    #                 ft.ElevatedButton(
    #
    #                     on_click=self.on_button_click,
    #                     content=ft.Text("1", size=40)
    #                 ),
    #
    #                 ft.ElevatedButton(
    #                     content=ft.Text("2", size=40),
    #                     on_click=self.on_button_click,
    #                 ),
    #                 ft.ElevatedButton(
    #                     content=ft.Text("3", size=40),
    #                     on_click=self.on_button_click,
    #                 ),
    #             ],
    #             alignment=ft.MainAxisAlignment.CENTER,
    #         ),
    #         ft.Row(
    #             [
    #                 ft.ElevatedButton(
    #                     content=ft.Text("4", size=40),
    #                     on_click=self.on_button_click,
    #
    #                 ),
    #                 ft.ElevatedButton(
    #                     content=ft.Text("5", size=40),
    #                     on_click=self.on_button_click,
    #                 ),
    #                 ft.ElevatedButton(
    #                     content=ft.Text("6", size=40),
    #                     on_click=self.on_button_click,
    #                 ),
    #             ],
    #             alignment=ft.MainAxisAlignment.CENTER,
    #         ),
    #         ft.Row(
    #             [
    #                 ft.ElevatedButton(
    #                     content=ft.Text("7", size=40),
    #                     on_click=self.on_button_click,
    #                 ),
    #                 ft.ElevatedButton(
    #                     content=ft.Text("8", size=40),
    #                     on_click=self.on_button_click,
    #                 ),
    #                 ft.ElevatedButton(
    #                     content=ft.Text("9", size=40),
    #                     on_click=self.on_button_click,
    #                 ),
    #             ],
    #             alignment=ft.MainAxisAlignment.CENTER,
    #         ),
    #         ft.Row(
    #             [
    #                 ft.ElevatedButton(
    #                     content=ft.Text("0", size=40),
    #                     on_click=self.on_button_click)
    #             ],
    #             alignment=ft.MainAxisAlignment.CENTER
    #         ),
    #     ],
    #     alignment=ft.alignment.center,
    #     horizontal_alignment=ft.CrossAxisAlignment.CENTER
    #
    # )

    async def validate(self, e):

        if all([len(self.user_login.value) >= 5,
                len(self.user_short_pass.value) >= 5,
                len(self.user_pass.value) >= 5]):
            self.button_reg.disabled = False
            print(self.button_reg.disabled)

        else:
            self.button_reg.disabled = True

        self.page.update()

    async def validate_short_aus_panel(self, e):
        k = len(self.row_stars.controls)
        if k == 5:
            self.button_short_aus.disabled = False
        else:
            self.button_short_aus.disabled = True

        self.page.update()


    async def auth_users(self, e):
        db = sqlite3.connect("id.base")
        cur = db.cursor()
        cur.execute(f"SELECT * FROM users WHERE login = '{self.user_login.value}' AND pass = '{self.user_pass.value}'")
        db.commit()
        a = cur.fetchone()

        if a != None:
            self.user_login.value = ""
            self.user_pass.value = ""
            await self.page.clean()
            await self.crete_home_content(e)
            self.page.snack_bar = ft.SnackBar(ft.Text("Добро пожаловать"))
            self.page.snack_bar.open = True


        else:
            self.button_aus.text = "Попробовать еще раз"

        db.close()
        self.page.update()

    async def short_uth_users(self, e):
        self.ki.append(e.control.content.value)
        if len(self.ki) == 5:
            short_key = "".join(self.ki)
            db = sqlite3.connect("id.base")
            cur = db.cursor()
            cur.execute(f"SELECT * FROM users WHERE short_pass = '{short_key}'")
            db.commit()

            keys = await self.page.client_storage.get_keys_async("")

            cur.execute(f"SELECT login FROM users")
            task = cur.fetchall()
            task = sum(task, ())
            task = list(task)

            keys1 = set(keys)
            task1 = set(task)
            resoult = keys1 & task1

            for task in resoult:
                res = await self.page.client_storage.get_async(task)

                cur.execute(f"SELECT login FROM users WHERE short_pass = '{short_key}' AND ide = '{res}'")
                r = cur.fetchall()
                if bool(r):

                    r = sum(r, ())
                    r = list(r)
                    self.user_login.value = ""
                    self.user_pass.value = ""
                    self.page.clean()
                    await self.crete_home_content(e)
                    self.page.snack_bar = ft.SnackBar(ft.Text(f"Добро пожаловать {r[0]}"))
                    self.page.snack_bar.open = True
                    break
                else:

                    self.ki.clear()
                    self.row_stars.controls.clear()
                    self.page.update()
                    self.page.snack_bar = ft.SnackBar(ft.Text(f"Попробуйте еще раз"))
                    self.page.snack_bar.open = True

            db.close()
            self.page.update()

    async def on_button_click(self, e):
        t = ft.Text("*", size=20)
        self.row_stars.controls.append(t)
        self.page.update()
        await self.validate_short_aus_panel(e)
        await self.short_uth_users(e)

    async def create_registration_panel(self,e):
        self.page.clean()
        await self.page.add_async(self.text,self.user_login,self.user_pass,self.user_short_pass, self.button_reg,
                            self.button_back_reg_panel)
        self.page.update()

    async def create_short_auth_panel(self, e):
        self.page.clean()
        await self.page.add_async(self.text3, self.f, self.row_stars, self.short_auth_panel,
                                  self.button_back_reg_panel)
        self.page.update()

    async def create_auth_panel(self, e):
        await self.page.clean()
        await self.page.add_async(self.text1,self.user_login,self.user_pass,self.button_aus,
                                  self.button_back_reg_panel)
        await self.page.update()

    async def get_key(self, e):
        self.ki.clear()
        self.row_stars.controls.clear()
        self.page.update()
        keys = await self.page.client_storage.get_keys_async("")

        db = sqlite3.connect("id.base")
        cur = db.cursor()
        cur.execute(f"SELECT login FROM users")
        task = cur.fetchall()
        task = sum(task, ())
        task = list(task)

        cur.execute(f"SELECT * FROM users ide")
        db.commit()
        k = cur.fetchall()
        k = sum(k, ())
        for key in keys:

            if key in k:
                await self.create_short_auth_panel(e)
                break
            else:
                await self.create_auth_panel(e)

        db.close()
    async def registration(self, e):
        await self.page.client_storage.clear_async()
        db = sqlite3.connect("id.base")
        cur = db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    login TEXT,
                    pass TEXT,
                    short_pass TEXT,
                    ide TEXT)""")

        key = str(random.randint(1000000000,9999999999))
        await self.page.client_storage.set_async(self.user_login.value, key)
        cur.execute(f"INSERT INTO users VALUES(NULL,'{self.user_login.value}','{self.user_pass.value}','{self.user_short_pass.value}','{key}')")
        db.commit()
        db.close()
        self.user_login.value = ""
        self.user_pass.value = ""
        self.user_short_pass.value = ""
        self.button_reg.text = "Добавлено"
        await self.crete_home_content(e)
        self.page.update()

    async def print_messages_from_base(self,e):
        self.page.clean()
        await self.page.add_async(self.button_back, self.button_clean)
        db = sqlite3.connect("id.base")
        cur = db.cursor()

        async def update_messages_from_base():
            cur.execute(f"SELECT * FROM messages")
            messages_base = cur.fetchall()
            for mes in messages_base:
                chat = ft.ListView(
                    padding=10,
                    spacing=10,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.START,
                            controls=[
                                Message(
                                    time=mes[2],
                                    author="Банк ПТБ (ООО):",
                                    body=mes[1])])])
                await self.page.add_async(chat)
                self.page.update()


        async def update_messages_from_PBS(message):
            now = datetime.datetime.now()
            time = str((now.strftime("%d.%m.%Y %H:%M:%S")))
            chat = ft.ListView(
                padding=10,
                spacing=10,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        controls=[
                            Message(
                                time=time,

                                author="Банк ПТБ (ООО):",
                                body=message)])])
            await self.page.add_async(chat)





        await update_messages_from_base()

        message_broker.subscribe(update_messages_from_PBS)
        db.close()
        self.page.update()


    async def clean_messages(self, e):
        await clean_massage_base()
        self.page.clean()
        await self.page.add_async(self.button_back, self.button_clean)
        self.page.update()
    async def change_theme_mode(self, e):
        self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
        self.page.update()

    async def crete_appbar(self):
        return ft.CupertinoAppBar(
            leading=ft.IconButton(ft.icons.ASSIGNMENT_IND, icon_size=20),
            trailing=ft.Row([
                ft.IconButton(ft.icons.SUNNY, on_click=self.change_theme_mode, icon_size=20),
                ft.Badge(content=ft.IconButton(ft.icons.DOORBELL, icon_size=20, on_click=self.print_messages_from_base),
                         text=await counter.count_message(0),label_visible=await counter.count_message1(0)),


            ],
                alignment=ft.MainAxisAlignment.END
            ))

    async def crete_start_appbar(self):
        return ft.CupertinoAppBar(

            trailing=ft.Row([
                ft.IconButton(content=ft.Text("Регистрация", size=12), on_click=self.create_registration_panel),
                ft.IconButton(content=ft.Text("Войти", size=12), on_click=self.get_key),
                ft.IconButton(ft.icons.SUNNY, on_click=self.change_theme_mode, icon_size=20),


            ],
                alignment=ft.MainAxisAlignment.END
            ))

    async def crete_home_content(self, e: ft.ControlEvent):
        self.page.clean()
        a = await self.crete_appbar()
        l = nav_content_corce.nav_content_corse()
        b = self.button_corse
        n = await navbar.nb.create_navigation_bar(e)
        await self.page.add_async(a,l,n)

    async def create_start_panel(self, e):
        a = await self.crete_start_appbar()
        self.page.clean()
        await self.page.add_async(a)
        self.page.update()