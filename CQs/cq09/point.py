from __future__ import annotations

"""CQ09 - Intro to OOP"""

__author__ = "730773852"


class Point:
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        self.x: float = 0.0
        self.y: float = 0.0

    # Mutation method
    def scale_by(self, factor: int) -> None:
        self.x *= factor
        self.y *= factor

    # No Mutation method
    def scale(self, factor: int) -> Point:
        return Point(self.x * factor, self.y * factor)
