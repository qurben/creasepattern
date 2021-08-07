import math

class Cp:
    def fromCp(filename):
        lines = []

        with open(filename, 'r') as cp:

            while True:
                next_line = cp.readline()

                if not next_line:
                    break;

                [type, x1, y1, x2, y2] = next_line.split(" ")

                cp_line = CpLine(int(type), float(x1), float(y1), float(x2), float(y2))

                lines.append(cp_line)

        return Cp(lines)

    def __init__(self, lines):
        self.lines = lines
        self.minX = 0
        self.maxX = 0
        self.minY = 0
        self.maxY = 0

        for cp_line in lines:
            if self.minX > cp_line.x1: self.minX = cp_line.x1
            if self.minX > cp_line.x2: self.minX = cp_line.x2
            if self.minY > cp_line.y1: self.minY = cp_line.y1
            if self.minY > cp_line.y2: self.minY = cp_line.y2

            if self.maxX < cp_line.x1: self.maxX = cp_line.x1
            if self.maxX < cp_line.x2: self.maxX = cp_line.x2
            if self.maxY < cp_line.y1: self.maxY = cp_line.y1
            if self.maxY < cp_line.y2: self.maxY = cp_line.y2


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
        if (self.type == 4 or self.type == 0):
            return (193, 193, 193)

        raise ValueError("Unknown line type in .cp file")

    def __str__(self) -> str:
        return "[type={}, x1={}, y1={}, x2={}, y2={}]".format(self.type, self.x1, self. y1, self.x2, self.y2)