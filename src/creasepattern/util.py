from .cp import CpLineType


def line_color(line_type: CpLineType):
    if line_type == CpLineType.EDGE:
        return 0, 0, 0
    if line_type == CpLineType.MOUNTAIN:
        return 255, 0, 0
    if line_type == CpLineType.VALLEY:
        return 0, 0, 255
    if line_type == CpLineType.AUX:
        return 193, 193, 193
    if line_type == CpLineType.AUX2:
        return 255, 200, 0
    if line_type == CpLineType.AUX3:
        return 255, 255, 0

    raise ValueError("Unknown line type " + line_type.value)


def line_color_rgb(line_type: CpLineType) -> str:
    r, g, b = line_color(line_type)

    return "rgb({}, {}, {})".format(r, g, b)


def line_width(line_type: CpLineType) -> int:
    if line_type == CpLineType.AUX2 or line_type == CpLineType.AUX3:
        return 3

    return 1
