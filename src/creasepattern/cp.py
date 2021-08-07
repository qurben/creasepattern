import math
from enum import Enum


class CpLineType(Enum):
    EDGE = 1
    MOUNTAIN = 2
    VALLEY = 3
    AUX = 4
    AUX2 = 5
    AUX3 = 8


class CpLine:
    def __init__(self, line_type: CpLineType, x1: float, y1: float, x2: float, y2: float) -> None:
        self.type = line_type
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self) -> str:
        return "[type={}, x1={}, y1={}, x2={}, y2={}]".format(self.type.name, self.x1, self.y1, self.x2, self.y2)


class CpCircle:
    def __init__(self, type: CpLineType, x: float, y: float, radius: float):
        self.type = type
        self.x = x
        self.y = y
        self.radius = radius


class BoundingBox:
    def __init__(self):
        self.minX = 0.0
        self.maxX = 0.0
        self.minY = 0.0
        self.maxY = 0.0

    def addX(self, *x):
        self.minX = min(self.minX, *x)
        self.maxX = max(self.maxX, *x)

    def addY(self, *y):
        self.minY = min(self.minY, *y)
        self.maxY = max(self.maxY, *y)

    @property
    def width(self):
        return self.maxX - self.minX

    @property
    def height(self):
        return self.maxY - self.minY


class Cp:
    def __init__(self, lines: list[CpLine], circles: list[CpCircle] = None):
        if circles is None:
            circles = []
        self.lines = lines
        self.circles = circles

        bb = BoundingBox()

        # Find the bounds
        for cp_line in lines:
            bb.addX(cp_line.x1, cp_line.x2)
            bb.addY(cp_line.y1, cp_line.y2)

        for circle in circles:
            bb.addX(circle.x - circle.radius, circle.x + circle.radius)
            bb.addY(circle.y - circle.radius, circle.y + circle.radius)

        self.bb = bb

    def size(self):
        width = math.ceil(self.bb.width)
        height = math.ceil(self.bb.height)

        return width, height
