"""Модуль приложения"""

import random
import time

import flet as ft

from .ball import Ball


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
