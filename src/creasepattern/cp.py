import math


class CpLine:
    def __init__(self, type: int, x1: float, y1: float, x2: float, y2: float) -> None:
        self.type = type
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def color(self):
        if (self.type == 1):
            return (0, 0, 0)
        if (self.type == 2):
            return (255, 0, 0)
        if (self.type == 3):
            return (0, 0, 255)
        if (self.type == 4 or self.type == 0):
            return (193, 193, 193)

        raise ValueError("Unknown line type " + self.type)

    def __str__(self) -> str:
        return "[type={}, x1={}, y1={}, x2={}, y2={}]".format(self.type, self.x1, self. y1, self.x2, self.y2)

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
    def __init__(self, lines: list[CpLine]):
        self.lines = lines
        self.minX = 0
        self.maxX = 0
        self.minY = 0
        self.maxY = 0

        bb = BoundingBox()

        # Find the bounds
        for cp_line in lines:
            bb.addX(cp_line.x1, cp_line.x2)
            bb.addY(cp_line.y1, cp_line.y2)
        self.bb = bb

    def size(self):
        width = math.ceil(self.bb.width)
        height = math.ceil(self.bb.height)

        return width, height
