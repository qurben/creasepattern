from .cp import Cp, CpLineType
from .util import line_color_rgb, line_width


def create_path(line_type: CpLineType, path: str) -> str:
    return '<path d="{}" stroke="{}" fill="none" stroke-width="{}" stroke-linecap="square"/>'.format(
        path,
        line_color_rgb(line_type),
        line_width(line_type),
    ) if path != "" else ""


def svg_float(f: float) -> str:
    return ('%.3f' % f).rstrip('0').rstrip('.')


def to_svg(cp: Cp, margin=10) -> str:
    """
    Convert a Cp object to an svg string
    """
    edge_path = ''
    mountain_path = ''
    valley_path = ''
    aux_path = ''
    aux2_path = ''
    aux3_path = ''
    for line in cp.lines:
        line_svg = "M{} {} L{} {}".format(
            svg_float(line.x1),
            svg_float(line.y1),
            svg_float(line.x2),
            svg_float(line.y2)
        )

        if line.type == CpLineType.EDGE:
            edge_path += line_svg

        if line.type == CpLineType.MOUNTAIN:
            mountain_path += line_svg

        if line.type == CpLineType.VALLEY:
            valley_path += line_svg

        if line.type == CpLineType.AUX:
            aux_path += line_svg

        if line.type == CpLineType.AUX2:
            aux2_path += line_svg

        if line.type == CpLineType.AUX3:
            aux3_path += line_svg

    for circle in cp.circles:
        circle_svg = """M {cx}, {cy} m {negR}, 0 a {r},{r} 0 1,0 {twoR},0 a {r},{r} 0 1,0 {negTwoR},0""".format(
            cx=svg_float(circle.x),
            cy=svg_float(circle.y),
            r=svg_float(circle.radius),
            negR=svg_float(-circle.radius),
            twoR=svg_float(2 * circle.radius),
            negTwoR=svg_float(-(2 * circle.radius))
        )

        if circle.type == CpLineType.EDGE:
            edge_path += circle_svg

        if circle.type == CpLineType.MOUNTAIN:
            mountain_path += circle_svg

        if circle.type == CpLineType.VALLEY:
            valley_path += circle_svg

        if circle.type == CpLineType.AUX:
            aux_path += circle_svg

        if circle.type == CpLineType.AUX2:
            aux2_path += circle_svg

        if circle.type == CpLineType.AUX3:
            aux3_path += circle_svg

    view_box = "{} {} {} {}".format(
        svg_float(cp.bb.minX - margin),
        svg_float(cp.bb.minY - margin),
        svg_float(cp.bb.maxX - cp.bb.minX + 2 * margin),
        svg_float(cp.bb.maxY - cp.bb.minY + 2 * margin),
    )

    edge_svg = create_path(CpLineType.EDGE, edge_path)
    mountain_svg = create_path(CpLineType.MOUNTAIN, mountain_path)
    valley_svg = create_path(CpLineType.VALLEY, valley_path)
    aux_svg = create_path(CpLineType.AUX, aux_path)
    aux2_svg = create_path(CpLineType.AUX2, aux2_path)
    aux3_svg = create_path(CpLineType.AUX3, aux3_path)

    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN" "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg version="1.0" xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="{viewBox}">
{}{}{}{}{}{}
</svg>""".format(
        edge_svg, mountain_svg, valley_svg, aux_svg, aux2_svg, aux3_svg,
        width=1024,
        height=1024,
        viewBox=view_box,
    )
