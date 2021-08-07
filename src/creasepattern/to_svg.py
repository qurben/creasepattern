from .cp import Cp


def svgFloat(f: float) -> str:
    return ('%.3f' % f).rstrip('0').rstrip('.')


def to_svg(cp: Cp, margin=10) -> str:
    """
    Convert a Cp object to an svg string
    """
    edgePath = ''
    mountainPath = ''
    valleyPath = ''
    auxPath = ''
    for line in cp.lines:
        lineSvg = "M{} {} L{} {}".format(
            svgFloat(line.x1),
            svgFloat(line.y1),
            svgFloat(line.x2),
            svgFloat(line.y2)
        )

        if (line.type == 1):
            edgePath += lineSvg

        if (line.type == 2):
            mountainPath += lineSvg

        if (line.type == 3):
            valleyPath += lineSvg

        if (line.type == 4):
            auxPath += lineSvg

    viewBox = "{} {} {} {}".format(
        svgFloat(cp.bb.minX-margin),
        svgFloat(cp.bb.minY-margin),
        svgFloat(cp.bb.maxX-cp.bb.minX+2*margin),
        svgFloat(cp.maxY-cp.minY+2*margin),
    )

    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN" "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg version="1.0" xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="{viewBox}">
<path d="{edgePath}" stroke="black"/>
<path d="{mountainPath}" stroke="red"/>
<path d="{valleyPath}" stroke="blue"/>
<path d="{auxPath}" stroke="grey"/>
</svg>""".format(
        width=1024,
        height=1024,
        viewBox=viewBox,
        edgePath=edgePath,
        mountainPath=mountainPath,
        valleyPath=valleyPath,
        auxPath=auxPath
    )
