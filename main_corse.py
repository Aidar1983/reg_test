import sqlite3
import datetime
import flet as ft
import flet.fastapi as flet_fastapi
import login_content
from message_sh import Message
from message_cls import message_broker


async def main_corse(page: ft.Page):
    page.scroll = "adaptive"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = "dark"
    # page.design = ft.PageDesign.ADAPTIVE
    page.window_width = "400"
    page.window_height = "700"
    page.window_resizable = False


    async def send_message_all(e):
        message = ft.TextField(hint_text="Текст сообщения...")

        now = datetime.datetime.now()
        time = str((now.strftime("%d.%m.%Y %H:%M:%S")))

        async def send_click(e):
            db = sqlite3.connect("id.base")
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS messages(
                                                            id INTEGER PRIMARY KEY,
                                                            message TEXT,
                                                            time TEXT)""")
            page.pubsub.send_all(f"{message.value}")
            cur.execute(f"INSERT INTO messages VALUES (NULL, '{message.value}', '{time}')")
            db.commit()
            await message_broker.send_all(message.value)
            message.value = ""


        messages = ft.Column()
        # прием сообщений из хранилища
        def on_message(msg):
            chat = ft.ListView(
                padding=10,
                spacing=10,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        controls=[
                            Message(
                                time=time,
                                author="Банк ПТБ(ООО):",
                                body=msg)])])
            messages.controls.append(chat)
            page.update()

        page.pubsub.subscribe(on_message)
        send = ft.ElevatedButton("Send", on_click=send_click)
        page.add(ft.Row(controls=[message, send]), messages)


    async def add_corse(e):
        db = sqlite3.connect("id.base")
        cur = db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS corses(
                                id INTEGER PRIMARY KEY,
                                usd_buy_ufa FLOAT,
                                usd_sell_ufa FLOAT,
                                eur_buy_ufa FLOAT,
                                eur_sell_ufa FLOAT,
                                cny_buy_ufa FLOAT,
                                cny_sell_ufa FLOAT,
                                usd_buy_rb FLOAT,
                                usd_sell_rb FLOAT,
                                eur_buy_rb FLOAT,
                                eur_sell_rb FLOAT,
                                cny_buy_rb FLOAT,
                                cny_sell_rb FLOAT,
                                usd_buy_msk FLOAT,
                                usd_sell_msk FLOAT,
                                eur_buy_msk FLOAT,
                                eur_sell_msk FLOAT)""")

        cur.execute(f"INSERT INTO corses VALUES (NULL, '{usd_buy_ufa.value}', "
                    f"'{usd_sell_ufa.value}', "
                    f"'{eur_buy_ufa.value}', "
                    f"'{eur_sell_ufa.value}', "
                    f"'{cny_buy_ufa.value}', "
                    f"'{cny_sell_ufa.value}', "
                    f"'{usd_buy_rb.value}', "
                    f"'{usd_sell_rb.value}', "
                    f"'{eur_buy_rb.value}', "
                    f"'{eur_sell_rb.value}', "
                    f"'{cny_buy_rb.value}', "
                    f"'{cny_sell_rb.value}', "
                    f"'{usd_buy_msk.value}', "
                    f"'{usd_sell_msk.value}', "
                    f"'{eur_buy_msk.value}', "
                    f"'{eur_sell_msk.value}' )")

        db.commit()

        button_add.text = "Добавлено"
        page.update()

    async def validate(e):
        if all([admin_login.value, admin_pass.value]):
            button_aus.disabled = False

        else:
            button_aus.disabled = True
        page.update()

    async def auth_admins(e):
        db = sqlite3.connect("id.base")
        cur = db.cursor()
        cur.execute(f"SELECT * FROM admins WHERE login = '{admin_login.value}' AND pass = '{admin_pass.value}'")
        db.commit()
        a = cur.fetchone()

        if a != None:
            admin_login.value = ""
            admin_pass.value = ""
            page.clean()
            await start_content(e)
            page.snack_bar = ft.SnackBar(ft.Text("Добро пожаловать"))
            page.snack_bar.open = True


        else:
            button_aus.text = "Попробовать еще раз"




    ufa = ft.Text("Установка курсов по Уфе:")
    usd_buy_ufa = ft.TextField(label="usd_buy_ufa", width=300)
    usd_sell_ufa = ft.TextField(label="usd_sell_ufa", width=300)
    eur_buy_ufa = ft.TextField(label="eur_buy_ufa", width=300)
    eur_sell_ufa = ft.TextField(label="eur_sell_ufa", width=300)
    cny_buy_ufa = ft.TextField(label="cny_buy_ufa", width=300)
    cny_sell_ufa = ft.TextField(label="cny_sell_ufa", width=300)
    rb = ft.Text("Установка курсов по РБ:")
    usd_buy_rb = ft.TextField(label="usd_buy_rb", width=300)
    usd_sell_rb = ft.TextField(label="usd_sell_rb", width=300)
    eur_buy_rb = ft.TextField(label="eur_buy_rb", width=300)
    eur_sell_rb = ft.TextField(label="eur_sell_rb", width=300)
    cny_buy_rb = ft.TextField(label="cny_buy_rb", width=300)
    cny_sell_rb = ft.TextField(label="cny_sell_rb", width=300)
    msk = ft.Text("Установка курсов по Москве:")
    usd_buy_msk = ft.TextField(label="usd_buy_msk", width=300)
    usd_sell_msk = ft.TextField(label="usd_sell_msk", width=300)
    eur_buy_msk = ft.TextField(label="eur_buy_msk", width=300)
    eur_sell_msk = ft.TextField(label="eur_sell_msk", width=300)
    button_add = ft.OutlinedButton("Добавить", width=200, on_click=add_corse, url="/")




    admin_login = ft.TextField(label="Логин", width=300, on_change=validate)
    admin_pass = ft.TextField(label="Пароль", width=300, on_change=validate)
    button_aus = ft.OutlinedButton("Авторизация", width=200, on_click=auth_admins, disabled=True)
    button_back = ft.OutlinedButton("Назад", width=200, url="/")

    await page.add_async(admin_login,admin_pass,button_aus, button_back)



    async  def start_content(e):
        page.clean()
        await page.add_async(button_corse, button_start_content_message)


    async def send_corse(e):

        await page.add_async(button_back,ufa,usd_buy_ufa,usd_sell_ufa,eur_buy_ufa,
                         eur_sell_ufa,cny_buy_ufa,cny_sell_ufa,rb,
                         usd_buy_rb,usd_sell_rb,eur_buy_rb,eur_sell_rb,
                         cny_buy_rb,cny_sell_rb, msk,usd_buy_msk,usd_sell_msk,
                         eur_buy_msk, eur_sell_msk,button_add)

    button_corse = ft.OutlinedButton("Установить курсы", width=200, on_click=send_corse)
    button_back = ft.OutlinedButton("Назад", width=200, on_click=start_content)


    async def message_content(e):
        button_send_all_message = ft.OutlinedButton("Отправить всем", width=200, on_click=send_message_all)
        button_send_choice_message = ft.OutlinedButton("Отправить по списку", width=200, on_click=message_content)
        page.clean()
        await page.add_async(button_send_all_message,button_send_choice_message)

    button_start_content_message = ft.OutlinedButton("Отправить сообщения", width=200, on_click=message_content)





# ft.app(target=main_corse)


