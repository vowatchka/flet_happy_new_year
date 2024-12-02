"""Модуль запуска приложения"""

import flet as ft
from app.app import HappyNewYearApp
from app.ball import Ball, BallInitParams
from app.constants import OFFSET_BOTTOM


def main(page: ft.Page):
    """Главная функция"""
    page.title = "С Новым Годом!"
    page.adaptive = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    app = HappyNewYearApp()
    page.add(app)

    # параметры инициализации шаров
    balls_init_params = [
        # 2
        BallInitParams(x=1, y=1, color=ft.Colors.RED),
        BallInitParams(x=2, y=0, color=ft.Colors.RED),
        BallInitParams(x=3, y=0, color=ft.Colors.RED),
        BallInitParams(x=4, y=1, color=ft.Colors.RED),
        BallInitParams(x=4, y=2, color=ft.Colors.RED),
        BallInitParams(x=3, y=3, color=ft.Colors.RED),
        BallInitParams(x=2, y=4, color=ft.Colors.RED),
        BallInitParams(x=1, y=5, color=ft.Colors.RED),
        BallInitParams(x=1, y=OFFSET_BOTTOM, color=ft.Colors.RED),
        BallInitParams(x=2, y=OFFSET_BOTTOM, color=ft.Colors.RED),
        BallInitParams(x=3, y=OFFSET_BOTTOM, color=ft.Colors.RED),
        BallInitParams(x=4, y=OFFSET_BOTTOM, color=ft.Colors.RED),
        # 0
        BallInitParams(x=8, y=0, color=ft.Colors.GREEN),
        BallInitParams(x=9, y=0, color=ft.Colors.GREEN),
        BallInitParams(x=10, y=1, color=ft.Colors.GREEN),
        BallInitParams(x=10, y=2, color=ft.Colors.GREEN),
        BallInitParams(x=10, y=3, color=ft.Colors.GREEN),
        BallInitParams(x=10, y=4, color=ft.Colors.GREEN),
        BallInitParams(x=10, y=5, color=ft.Colors.GREEN),
        BallInitParams(x=9, y=OFFSET_BOTTOM, color=ft.Colors.GREEN),
        BallInitParams(x=8, y=OFFSET_BOTTOM, color=ft.Colors.GREEN),
        BallInitParams(x=7, y=5, color=ft.Colors.GREEN),
        BallInitParams(x=7, y=4, color=ft.Colors.GREEN),
        BallInitParams(x=7, y=3, color=ft.Colors.GREEN),
        BallInitParams(x=7, y=2, color=ft.Colors.GREEN),
        BallInitParams(x=7, y=1, color=ft.Colors.GREEN),
        # 2
        BallInitParams(x=13, y=1, color=ft.Colors.BLUE),
        BallInitParams(x=14, y=0, color=ft.Colors.BLUE),
        BallInitParams(x=15, y=0, color=ft.Colors.BLUE),
        BallInitParams(x=16, y=1, color=ft.Colors.BLUE),
        BallInitParams(x=16, y=2, color=ft.Colors.BLUE),
        BallInitParams(x=15, y=3, color=ft.Colors.BLUE),
        BallInitParams(x=14, y=4, color=ft.Colors.BLUE),
        BallInitParams(x=13, y=5, color=ft.Colors.BLUE),
        BallInitParams(x=13, y=OFFSET_BOTTOM, color=ft.Colors.BLUE),
        BallInitParams(x=14, y=OFFSET_BOTTOM, color=ft.Colors.BLUE),
        BallInitParams(x=15, y=OFFSET_BOTTOM, color=ft.Colors.BLUE),
        BallInitParams(x=16, y=OFFSET_BOTTOM, color=ft.Colors.BLUE),
        # 5
        BallInitParams(x=22, y=0, color=ft.Colors.PURPLE),
        BallInitParams(x=21, y=0, color=ft.Colors.PURPLE),
        BallInitParams(x=20, y=0, color=ft.Colors.PURPLE),
        BallInitParams(x=19, y=0, color=ft.Colors.PURPLE),
        BallInitParams(x=19, y=1, color=ft.Colors.PURPLE),
        BallInitParams(x=19, y=2, color=ft.Colors.PURPLE),
        BallInitParams(x=20, y=2, color=ft.Colors.PURPLE),
        BallInitParams(x=21, y=2, color=ft.Colors.PURPLE),
        BallInitParams(x=22, y=3, color=ft.Colors.PURPLE),
        BallInitParams(x=22, y=4, color=ft.Colors.PURPLE),
        BallInitParams(x=22, y=5, color=ft.Colors.PURPLE),
        BallInitParams(x=21, y=OFFSET_BOTTOM, color=ft.Colors.PURPLE),
        BallInitParams(x=20, y=OFFSET_BOTTOM, color=ft.Colors.PURPLE),
        BallInitParams(x=19, y=5, color=ft.Colors.PURPLE),
    ]

    for init_params in balls_init_params:
        ball = Ball(init_params=init_params)
        app.add_ball(ball)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
