from .cp import Cp, CpLineType
from .util import line_color_rgb, line_width


def to_svg(cp: Cp) -> str:
    """
    Convert a Cp object to a cp file string.
    """
    cp_str = ''
    for line in cp.lines:
        cp_str += line.type.value + " " + line.x1 + " " + line.y1 + " " + line.x2 + " " + line.y2 + "\n"

    return cp_str
