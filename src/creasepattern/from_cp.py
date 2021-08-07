from typing import List

from .cp import Cp, CpLine, CpLineType


def from_cp(filename: str) -> Cp:
    """
    Load a .cp file
    """
    lines = []

    with open(filename, 'r') as cp:

        while True:
            next_line = cp.readline()

            if not next_line:
                break

            [type, x1, y1, x2, y2] = next_line.split(" ")

            cp_line = CpLine(CpLineType(int(type)), float(
                x1), float(y1), float(x2), float(y2))

            lines.append(cp_line)

    return Cp(lines)


def from_cp_str(lines: List[str]) -> Cp:
    """
    Load the .cp file format from a string
    """
    cp_lines = []

    for line in lines:
        [line_type, x1, y1, x2, y2] = line.split(" ")

        cp_line = CpLine(CpLineType(int(line_type)), float(
            x1), float(y1), float(x2), float(y2))

        cp_lines.append(cp_line)

    return Cp(cp_lines)
