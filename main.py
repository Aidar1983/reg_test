
import random

import flet as ft
import flet.fastapi as flet_fastapi
import nav_content_corce
from main_corse import main_corse
import navbar
import login_content



app = flet_fastapi.FastAPI()

c = random.randint(1, 100)
async def main(page: ft.Page):
    page.clean()
    page.title = "Банк ПТБ (ООО)"
    page.scroll = "adaptive"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = "dark"
    page.adaptive = True
    # page.design = ft.PageDesign.ADAPTIVE
    page.window_width = "400"
    page.window_height = "700"
    page.window_resizable = False


    page.update()


    # f = ft.Text("Введите код-пароль", size=20)
    # ki = []
    # row_stars = ft.Row(alignment=ft.MainAxisAlignment.CENTER)
    #
    # async def on_button_click(e):
    #     t = ft.Text("*", size=20)
    #     row_stars.controls.append(t)
    #     page.update()
    #     await validate_short_aus_panel(e)
    #     await short_uth_users(e)
    #
    #
    # async def get_key(e):
    #     ki.clear()
    #     row_stars.controls.clear()
    #     page.update()
    #     keys = await page.client_storage.get_keys_async("")
    #
    #     db = sqlite3.connect("id.base")
    #     cur = db.cursor()
    #     cur.execute(f"SELECT login FROM users")
    #     task = cur.fetchall()
    #     task = sum(task, ())
    #     task = list(task)
    #
    #     cur.execute(f"SELECT * FROM users ide")
    #     db.commit()
    #     k = cur.fetchall()
    #     k = sum(k, ())
    #     for key in keys:
    #
    #         if key in k:
    #             await create_short_auth_panel(e)
    #             break
    #         else:
    #             await create_auth_panel(e)
    #
    #     db.close()
    #
    # async def change_theme_mode(e):
    #     page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
    #     page.update()
    #
    # async def registration(e):
    #     await page.client_storage.clear_async()
    #     db = sqlite3.connect("id.base")
    #     cur = db.cursor()
    #     cur.execute("""CREATE TABLE IF NOT EXISTS users(
    #                 id INTEGER PRIMARY KEY,
    #                 login TEXT,
    #                 pass TEXT,
    #                 short_pass TEXT,
    #                 ide TEXT)""")
    #
    #     key = str(random.randint(1000000000,9999999999))
    #     await page.client_storage.set_async(user_login.value, key)
    #     cur.execute(f"INSERT INTO users VALUES(NULL,'{user_login.value}','{user_pass.value}','{user_short_pass.value}','{key}')")
    #     db.commit()
    #     db.close()
    #     user_login.value = ""
    #     user_pass.value = ""
    #     user_short_pass.value = ""
    #     button_reg.text = "Добавлено"
    #     await start_home(e)
    #     page.update()
    #
    # async def start_home(e):
    #     await home(e)
    #
    # async def start_create_start_panel(e):
    #     await create_start_panel(e)
    #
    # async def short_uth_users(e):
    #     ki.append(e.control.content.value)
    #     if len(ki) == 5:
    #         short_key = "".join(ki)
    #         db = sqlite3.connect("id.base")
    #         cur = db.cursor()
    #         cur.execute(f"SELECT * FROM users WHERE short_pass = '{short_key}'")
    #         db.commit()
    #
    #         keys = await page.client_storage.get_keys_async("")
    #
    #         cur.execute(f"SELECT login FROM users")
    #         task = cur.fetchall()
    #         task = sum(task, ())
    #         task = list(task)
    #
    #         keys1 = set(keys)
    #         task1 = set(task)
    #         resoult = keys1 & task1
    #
    #         for task in resoult:
    #             res = await page.client_storage.get_async(task)
    #
    #             cur.execute(f"SELECT login FROM users WHERE short_pass = '{short_key}' AND ide = '{res}'")
    #             r = cur.fetchall()
    #             if bool(r):
    #
    #                 r = sum(r, ())
    #                 r = list(r)
    #                 user_login.value = ""
    #                 user_pass.value = ""
    #                 page.clean()
    #                 await start_home(e)
    #                 page.snack_bar = ft.SnackBar(ft.Text(f"Добро пожаловать {r[0]}"))
    #                 page.snack_bar.open = True
    #                 break
    #             else:
    #
    #                 ki.clear()
    #                 row_stars.controls.clear()
    #                 page.update()
    #                 page.snack_bar = ft.SnackBar(ft.Text(f"Попробуйте еще раз"))
    #                 page.snack_bar.open = True
    #
    #         db.close()
    #         page.update()
    #
    # async def auth_users(e):
    #     db = sqlite3.connect("id.base")
    #     cur = db.cursor()
    #     cur.execute(f"SELECT * FROM users WHERE login = '{user_login.value}' AND pass = '{user_pass.value}'")
    #     db.commit()
    #     a = cur.fetchone()
    #
    #     if a != None:
    #         user_login.value = ""
    #         user_pass.value = ""
    #         await page.clean()
    #         await start_home(e)
    #         page.snack_bar = ft.SnackBar(ft.Text("Добро пожаловать"))
    #         page.snack_bar.open = True
    #
    #
    #     else:
    #         button_aus.text = "Попробовать еще раз"
    #
    #     db.close()
    #     page.update()
    #
    #
    #
    # async def validate(e):
    #     if all([len(user_login.value) >= 5, len(user_pass.value) >= 5, len(user_short_pass.value) >= 5]):
    #         button_reg.disabled = False
    #         page.update()
    #
    #     else:
    #         button_reg.disabled = True
    #         page.update()
    #
    #     page.update()
    #
    # async def validate_short_aus_panel(e):
    #     k = len(row_stars.controls)
    #     if k == 5:
    #         button_short_aus.disabled = False
    #     else:
    #         button_short_aus.disabled = True
    #
    #     page.update()
    #
    #
    #
    # async def crete_appbar():
    #     return ft.CupertinoAppBar(
    #         leading=ft.IconButton(ft.icons.ASSIGNMENT_IND, icon_size=20),
    #         trailing=ft.Row([
    #             ft.IconButton(content=ft.Text("Регистрация", size=12), on_click=create_registration_panel),
    #             ft.IconButton(content=ft.Text("Войти", size=12), on_click=get_key),
    #             ft.IconButton(ft.icons.SUNNY, on_click=change_theme_mode, icon_size=20),
    #             ft.Badge(content=ft.IconButton(ft.icons.DOORBELL, icon_size=20),
    #                                   text="1"),
    #
    #
    #         ],
    #             alignment=ft.MainAxisAlignment.END
    #         ))
    #
    #
    # text = ft.Text("Регистрация")
    # text1 = ft.Text("Авторизация")
    # text3 = ft.Text("Упрощенная авторизация")
    # user_login = ft.TextField(label="Логин", width=300, on_change=validate)
    # user_pass = ft.TextField(label="Пароль", password=True, width=300, on_change=validate)
    # user_short_pass = ft.TextField(label="Ведите короткий пароль (5 цифр)", password=True, width=300,
    #                                on_change=validate_short_aus_panel)
    # button_reg = ft.OutlinedButton("Регистрация", width=200, on_click=registration, disabled=True)
    # button_aus = ft.OutlinedButton("Авторизация", width=200, on_click=auth_users)
    # button_back = ft.OutlinedButton("Назад", width=200, on_click=start_home)
    # button_back_reg_panel = ft.OutlinedButton("Выйти", width=200, on_click=start_create_start_panel)
    # button_short_aus = ft.OutlinedButton("Авторизация", width=200, on_click= short_uth_users, disabled=True)
    # button_corse = ft.OutlinedButton("Установить курсы", width=200, url="/corse/")
    # short_auth_panel = ft.Column(
    #     [
    #         ft.Row(
    #             [
    #                 ft.ElevatedButton(
    #
    #                     on_click=on_button_click,
    #                     content=ft.Text("1", size=40)
    #                 ),
    #
    #                 ft.ElevatedButton(
    #                     content=ft.Text("2", size=40),
    #                     on_click=on_button_click,
    #                 ),
    #                 ft.ElevatedButton(
    #                     content=ft.Text("3", size=40),
    #                     on_click=on_button_click,
    #                 ),
    #             ],
    #             alignment=ft.MainAxisAlignment.CENTER,
    #         ),
    #         ft.Row(
    #             [
    #                 ft.ElevatedButton(
    #                     content=ft.Text("4", size=40),
    #                     on_click=on_button_click,
    #
    #                 ),
    #                 ft.ElevatedButton(
    #                     content=ft.Text("5", size=40),
    #                     on_click=on_button_click,
    #                 ),
    #                 ft.ElevatedButton(
    #                     content=ft.Text("6", size=40),
    #                     on_click=on_button_click,
    #                 ),
    #             ],
    #             alignment=ft.MainAxisAlignment.CENTER,
    #         ),
    #         ft.Row(
    #             [
    #                 ft.ElevatedButton(
    #                     content=ft.Text("7", size=40),
    #                     on_click=on_button_click,
    #                 ),
    #                 ft.ElevatedButton(
    #                     content=ft.Text("8", size=40),
    #                     on_click=on_button_click,
    #                 ),
    #                 ft.ElevatedButton(
    #                     content=ft.Text("9", size=40),
    #                     on_click=on_button_click,
    #                 ),
    #             ],
    #             alignment=ft.MainAxisAlignment.CENTER,
    #         ),
    #         ft.Row(
    #             [
    #                 ft.ElevatedButton(
    #                     content=ft.Text("0", size=40),
    #                     on_click=on_button_click)
    #             ],
    #             alignment=ft.MainAxisAlignment.CENTER
    #         ),
    #     ],
    #
    #     alignment=ft.alignment.center,
    #     horizontal_alignment=ft.CrossAxisAlignment.CENTER
    #
    # )
    #
    #
    # async def create_registration_panel(e):
    #     page.clean()
    #     await page.add_async(text,user_login,user_pass,user_short_pass, button_reg, button_back_reg_panel)
    #     page.update()
    #
    # async def create_auth_panel(e):
    #     await page.clean()
    #     await page.add_async(text1,user_login,user_pass,button_aus, button_back_reg_panel)
    #     await page.update()
    #
    # async def create_short_auth_panel(e):
    #     page.clean()
    #     await page.add_async(text3,f,row_stars, short_auth_panel, button_back_reg_panel)
    #     page.update()
    #
    # async def create_start_panel(e):
    #     page.clean()
    #     await page.add_async(a)
    #     page.update()
    #
    # async def home(e):
    #     page.clean()
    #     await crete_home_content(e)
    #
    #
    # async def crete_home_content(e):
    #     page.clean()
    #     a = await crete_appbar()
    #     l = nav_content_corce.nav_content_corse()
    #     b = button_corse
    #     n = await navbar.nb.create_navigation_bar(e)
    #
    #
    #
    #     await page.add_async(a,l,b,n)

    # page.on_scroll = await crete_home_content(e)

    start = login_content.Constructor(page)
    a = await start.crete_start_appbar()




    await page.add_async(a)


# ft.app(target=main)


app.mount("/corse", flet_fastapi.app(main_corse))
app.mount("/", flet_fastapi.app(main))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

# flet run --ios