"""Модуль приложения"""

import random
import time

import flet as ft

from .ball import Ball


class AppHeader(ft.Container):
    """Класс хедэра приложения"""

    def __init__(self):
        super().__init__()

        self.margin = ft.margin.symmetric(horizontal=100, vertical=20)

        self.git_button = self._create_button(
            text="Developed by vowatchka",
            image_src="imgs/git-icon.webp",
            image_size=24,
            on_click=self.open_github,
        )

        self.cloudflare_button = self._create_button(
            text="Hosted by Cloudflare",
            image_src="imgs/cloudflare-icon.png",
            image_size=30,
            on_click=self.open_cloudflare,
        )

        self.content = ft.Row(
            controls=[self.git_button, self.cloudflare_button],
            alignment=ft.MainAxisAlignment.END,
            expand=True,
        )

    def open_cloudflare(self, e: ft.ControlEvent):
        """Открыть ссылку на Cloudflare"""
        e.control.page.launch_url("https://dash.cloudflare.com/")

    def open_github(self, e: ft.ControlEvent):
        """Открыть ссылку на Git"""
        e.control.page.launch_url("https://github.com/vowatchka")

    @staticmethod
    def _create_button(
        text: str,
        image_src: str,
        image_size: int,
        on_click: ft.core.types.OptionalControlEventCallable = None
    ):
        """Создать кнопку"""
        text_style = ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)
        button_style = ft.ButtonStyle(color=ft.Colors.BLUE, text_style=text_style)

        return ft.TextButton(
            style=button_style,
            content=ft.Row(
                controls=[
                    ft.Image(src=image_src, width=image_size, height=image_size),
                    ft.Text(value=text, style=text_style),
                ],
            ),
            on_click=on_click,
        )


class HappyNewYearApp(ft.Column):
    """Класс приложения"""

    def __init__(self):
        super().__init__()

        self.run_again = False

        self.balls: list[Ball] = []
        self.dropped_balls: list[Ball] = []

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.expand = True

        self.app_header = AppHeader()

        self.stack = ft.Stack(
            width=1000,
            height=280,
        )
        self.go_button = ft.ElevatedButton(text="Go!", on_click=self.go)
        self.again_button = ft.ElevatedButton(text="Again!", on_click=self.again)
        self.again_button.visible = False

        self.app_view = ft.Column(
            controls=[
                self.stack,
                ft.Row(
                    controls=[self.go_button, self.again_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            width=self.stack.width,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=70,
            expand=True,
        )

        self.controls = [
            self.app_header,
            self.app_view,
        ]

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

            time.sleep(0.03)
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

            time.sleep(0.03)
            self.again(e)
        else:
            self.setup_buttons(None)
            self.run_again = False
