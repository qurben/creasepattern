from .cp import Cp, CpLine

def from_cp(filename) -> Cp:
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