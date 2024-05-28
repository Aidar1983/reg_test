import sqlite3

import flet as ft
from flet_core import TextThemeStyle

def nav_content_corse():
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

    cur.execute(f"SELECT * FROM corses ORDER BY id DESC LIMIT 1")
    db.commit()
    corse = cur.fetchone()
    db.close()

    return ft.Column(

                [
                    ft.Text("Курсы валют", size=15, style=TextThemeStyle.HEADLINE_SMALL,
                            ),

                    ft.Row(
                        [

                        ft.Container(
                            content=ft.Column([
                                ft.Row([ft.Text("Курсы по офисам в г. Уфа", size=17, color="black")],alignment=ft.MainAxisAlignment.CENTER),
                                ft.Row([ft.Text("Валюта", size=14, color="black"),
                                        ft.Text("Покупка", size=14, color="black"),
                                        ft.Text("Продажа", size=14, color="black")],
                                       alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                                ft.Row([ft.Text("USD", size=14, color="black"),
                                        ft.Text(corse[1], size=14, color="black"),
                                        ft.Text(corse[2], size=14, color="black")],
                                       alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                                ft.Row([ft.Text("EUR", size=14, color="black"),
                                        ft.Text(corse[3], size=14, color="black"),
                                        ft.Text(corse[4], size=14, color="black")],
                                       alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                                ft.Row([ft.Text("CNY", size=14, color="black"),
                                        ft.Text(corse[5], size=14, color="black"),
                                        ft.Text(corse[6], size=14, color="black")],
                                       alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                            ]

                            ),

                            bgcolor=ft.colors.WHITE,
                            # border_radius=ft.border_radius.all(5),
                            width=360,
                            height=170,
                            margin=10,
                            padding=10,
                            alignment=ft.alignment.center,
                            border_radius=10,
                            ink=True),

                        ft.Container(
                            content=ft.Column([
                                ft.Row([ft.Text("Курсы по офисам в РБ", size=17, color="black")],alignment=ft.MainAxisAlignment.CENTER),
                                ft.Row([ft.Text("Валюта", size=14, color="black"),
                                        ft.Text("Покупка", size=14, color="black"),
                                        ft.Text("Продажа", size=14, color="black")],
                                       alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                                ft.Row([ft.Text("USD", size=14, color="black"),
                                        ft.Text(corse[7], size=14, color="black"),
                                        ft.Text(corse[8], size=14, color="black")],
                                       alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                                ft.Row([ft.Text("EUR", size=14, color="black"),
                                        ft.Text(corse[9], size=14, color="black"),
                                        ft.Text(corse[10], size=14, color="black")],
                                       alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                                ft.Row([ft.Text("CNY", size=14, color="black"),
                                        ft.Text(corse[11], size=14, color="black"),
                                        ft.Text(corse[12], size=14, color="black")],
                                       alignment=ft.MainAxisAlignment.SPACE_EVENLY)
                            ]

                            ),

                            bgcolor=ft.colors.WHITE,
                            # border_radius=ft.border_radius.all(5),
                            width=360,
                            height=170,
                            margin=10,
                            padding=10,
                            alignment=ft.alignment.center,
                            border_radius=10,
                            ink=True),

                        ft.Container(
                            content=ft.Column([
                                ft.Row([ft.Text("Курсы по офисам в г. Москва", size=17, color="black")],alignment=ft.MainAxisAlignment.CENTER),
                                ft.Row([ft.Text("Валюта", size=14,color="black"),ft.Text("Покупка", size=14,color="black"),ft.Text("Продажа", size=14,color="black")], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                                ft.Row([ft.Text("USD", size=14, color="black"), ft.Text(corse[13], size=14, color="black"),ft.Text(corse[14], size=14, color="black")],alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                                ft.Row([ft.Text("EUR", size=14, color="black"), ft.Text(corse[15], size=14, color="black"),ft.Text(corse[16], size=14, color="black")],alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                                        ]

                            ),

                            bgcolor=ft.colors.WHITE,
                            # border_radius=ft.border_radius.all(5),
                            width=360,
                            height=170,
                            margin=10,
                            padding=10,
                            alignment=ft.alignment.center,
                            border_radius=10,
                            ink=True)


                    ],
                    scroll=ft.ScrollMode.HIDDEN

                    )


                ])