from enum import Enum
from .cp import Cp, CpCircle, CpLine, CpLineType


class OrihimeSegmentSet(Enum):
    NONE = 0
    LINE = 1
    AUX = 2
    CIRCLE = 3


def from_orh(filename: str) -> Cp:
    cp_lines = []
    cp_circles = []
    with open(filename, 'r', encoding='utf-8') as cp:
        line_type = 0
        mode = OrihimeSegmentSet.NONE

        while True:
            line = cp.readline().rstrip()

            if not line:
                break

            if len(line) != 0:
                tokens = line.split(',')
                string = tokens[0]

                if string == "<線分集合>":  # translates to "line segment set"
                    mode = OrihimeSegmentSet.LINE
                    continue
                if string == "<補助線分集合>":  # translates to "auxiliary line segment set"
                    mode = OrihimeSegmentSet.AUX
                    continue
                if string == "<円集合>":  # translates to "circle set"
                    mode = OrihimeSegmentSet.CIRCLE
                    continue

                if mode == OrihimeSegmentSet.LINE:
                    if string == "色":  # translates to "colour"
                        line_type = int(tokens[1]) + 1
                    if string == "座標":  # translates to "coordinate"
                        d1 = float(tokens[1])
                        d2 = float(tokens[2])
                        d3 = float(tokens[3])
                        d4 = float(tokens[4])

                        cp_line = CpLine(CpLineType(line_type), d1, d2, d3, d4)
                        cp_lines.append(cp_line)
                if mode == OrihimeSegmentSet.CIRCLE:
                    if string == "中心と半径と色":  # translates to "Center, radius and color"
                        x = float(tokens[1])
                        y = float(tokens[2])
                        radius = float(tokens[3])
                        line_type = float(tokens[4]) + 1

                        cp_circles.append(CpCircle(CpLineType(line_type), x, y, radius))

                if mode == OrihimeSegmentSet.AUX:
                    if string == "補助色":  # translates to "Auxiliary color"
                        line_type = int(tokens[1]) + 1
                    if string == "補助座標":  # translates to "Auxiliary coordinates"
                        d1 = float(tokens[1])
                        d2 = float(tokens[2])
                        d3 = float(tokens[3])
                        d4 = float(tokens[4])

                        cp_lines.append(CpLine(CpLineType(line_type), d1, d2, d3, d4))

    return Cp(cp_lines, cp_circles)
