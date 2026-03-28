import math
import random

class Rectangle:
    def __init__(self, x: float, y: float, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина і висота мають бути > 0")
        self.x = round(x, 2)
        self.y = round(y, 2)
        self.width = round(width, 2)
        self.height = round(height, 2)
 

    def perimeter(self) -> float:
        return round(2 * (self.width + self.height), 2)
 

    def area(self) -> float:
        return round(self.width * self.height, 2)
 

    def key(self) -> int:
        return round(self.perimeter())
 

    def __str__(self) -> str:
        return (f"Rect[({self.x}, {self.y}), "
                f"w={self.width}, h={self.height}, "
                f"P={self.perimeter()}, S={self.area()}]")
 

    @staticmethod
    def random_rectangle(max_coord: float = 10.0, max_side: float = 10.0) -> "Rectangle":
        x = round(random.uniform(0, max_coord), 2)
        y = round(random.uniform(0, max_coord), 2)
        w = round(random.uniform(0.5, max_side), 2)
        h = round(random.uniform(0.5, max_side), 2)
        return Rectangle(x, y, w, h)
 