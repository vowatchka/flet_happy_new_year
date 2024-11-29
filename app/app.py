"""Модуль приложения"""

import random
import time

import flet as ft

from ball import Ball, BallInitParams
from constants import OFFSET_BOTTOM


class HappyNewYearApp(ft.Row):
    """Класс приложения"""

    def __init__(self):
        super().__init__()

        self.run_again = False

        self.balls: list[Ball] = []
        self.dropped_balls: list[Ball] = []

        self.stack = ft.Stack(
            width=1000,
            height=280,
        )
        self.go_button = ft.ElevatedButton(text="Go!", on_click=self.go)
        self.again_button = ft.ElevatedButton(text="Again!", on_click=self.again)
        self.again_button.visible = False

        self.alignment = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER

        self.controls.append(self.stack)

    def add(self, control: ft.Control):
        """Добавить элемент управления"""
        self.stack.controls.append(control)
        self.update()

    def add_ball(self, ball: Ball):
        """Добавить шар"""
        self.balls.append(ball)
        self.add(ball)

    def setup_buttons(self, e: ft.ControlEvent):
        """Настройка кнопок"""
        self.again_button.visible = False
        self.again_button.disabled = False
        self.again_button.update()

        self.go_button.visible = True
        self.go_button.update()

    def go(self, e: ft.ControlEvent):
        """Запустить анимацию"""
        if self.run_again:
            return

        if self.go_button.visible:
            self.go_button.visible = False
            self.go_button.update()

        if not self.again_button.visible:
            self.again_button.visible = True
            self.again_button.update()

        if len(self.balls):
            idx = random.randint(0, len(self.balls) - 1)
            ball = self.balls.pop(idx)
            self.dropped_balls.append(ball)

            ball.drop()

            time.sleep(0.01)
            self.go(e)

    def again(self, e: ft.ControlEvent):
        """Повторить анимацию"""
        if not self.run_again:
            self.run_again = True
            self.setup_buttons(None)

        if len(self.dropped_balls):
            idx = random.randint(0, len(self.dropped_balls) - 1)
            ball = self.dropped_balls.pop(idx)
            self.balls.append(ball)

            ball.restore()

            time.sleep(0.01)
            self.again(e)
        else:
            self.setup_buttons(None)
            self.run_again = False


def main(page: ft.Page):
    """Главная функция"""
    page.title = "С Новым Годом!"
    page.adaptive = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 70

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

    page.add(app.go_button, app.again_button)


if __name__ == "__main__":
    ft.app(target=main, port=8000, assets_dir="assets")
