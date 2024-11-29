"""Модуль шара"""

import random
from dataclasses import dataclass
import flet as ft

from .constants import OFFSET_BOTTOM


@dataclass
class BallInitParams:
    """Параметры инициализации шара"""

    x: int
    y: int
    color: str


class Ball(ft.Stack):
    """Класс шара"""

    def __init__(self, init_params: BallInitParams):
        super().__init__(offset=ft.Offset(x=init_params.x, y=init_params.y))

        self.init_params = init_params

        # на сколько смещать по оси X
        self.change_x = None
        # максимальная координата по оси X
        self.max_x = None

        self.opacity = 0.7
        self.rotate = ft.Rotate(angle=0)

        self.offset_animation = ft.animation.Animation(
            duration=1000,
            curve=ft.animation.AnimationCurve.EASE_IN_BACK,
        )
        self.rotate_animation = ft.animation.Animation(
            duration=700,
            curve=ft.animation.AnimationCurve.LINEAR,
        )
        self.setup_animation(None)

        self.controls = [
            # шар
            ft.Container(
                width=40,
                height=40,
                border_radius=40,
                bgcolor=init_params.color,
            ),
            # большой блик
            ft.Container(
                width=7,
                height=7,
                border_radius=7,
                bgcolor=ft.Colors.WHITE,
                opacity=0.9,
                top=7,
                left=27,
            ),
            # маленький блик
            ft.Container(
                width=4,
                height=4,
                border_radius=4,
                bgcolor=ft.Colors.WHITE,
                opacity=0.9,
                top=15,
                left=31,
            ),
        ]

    def setup_animation(self, e: ft.ControlEvent):
        """Настройка анимации шара"""
        self.animate_offset = self.offset_animation
        self.animate_rotation = self.rotate_animation
        self.on_animation_end = self.roll

    def drop(self):
        """Падение шара"""
        self.setup_animation(None)
        self.offset.y = OFFSET_BOTTOM
        self.update()

    def restore(self):
        """Вернуть шар на место"""
        # сбрасываем анимации качения
        self.animate_rotation = None
        self.on_animation_end = None

        self.offset.x = self.init_params.x
        self.offset.y = self.init_params.y

        self.update()

    def roll(self, e: ft.ControlEvent):
        """Катить шар"""
        self.animate_offset = self.animate_rotation

        self.rotate.angle += 1
        if self.rotate.angle == 361:
            self.rotate.angle = 1

        if not self.change_x:
            self.change_x = random.choice((-1, 1))
            if self.change_x < 0:
                self.max_x = random.randint(-3, self.offset.x + self.change_x)
            else:
                self.max_x = random.randint(self.offset.x + self.change_x, 26)

        self.offset.x += self.change_x
        if self.offset.x == self.max_x:
            self.on_animation_end = None

        self.update()
