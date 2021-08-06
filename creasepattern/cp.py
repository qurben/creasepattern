import math

class Cp:
    def __init__(self, filename):
        with open(filename, 'r') as cp:
            lines = cp.readlines()

        lines = [line.split(' ') for line in lines]
        self.lines = [CpLine(int(type), float(x1), float(y1), float(
            x2), float(y2)) for [type, x1, y1, x2, y2] in lines]

        xVals = sum([[x.x1, x.x2] for x in self.lines], [])
        yVals = sum([[x.y1, x.y2] for x in self.lines], [])

        self.minX = min(xVals)
        self.maxX = max(xVals)
        self.minY = min(yVals)
        self.maxY = max(yVals)

    def size(self):
        width = math.ceil(self.maxX-self.minX)
        height = math.ceil(self.maxY-self.minY)

        return width, height


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
        if (self.type == 4):
            return (193, 193, 193)

        raise ValueError("Unknown line type in .cp file")