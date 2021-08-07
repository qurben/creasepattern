
from .cp import Cp, CpLine
import defusedxml.ElementTree as ET


def from_orh(filename: str) -> Cp:
    cp_lines = []
    with open(filename, 'r', encoding='utf-8') as cp:
        type = 0

        while True:
            line = cp.readline()

            if not line:
                break

            if (len(line) != 0):
                toks = line.split(',')
                string = toks[0]

                if string == "色": # translates to "colour"
                    type = int(toks[1]) + 1
                if string == "座標": # translates to "coordinate"
                    d1 = float(toks[1])
                    d2 = float(toks[2])
                    d3 = float(toks[3])
                    d4 = float(toks[4])

                    cp_line = CpLine(type, d1, d2, d3, d4)
                    cp_lines.append(cp_line)

    return Cp(cp_lines)
