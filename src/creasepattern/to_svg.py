from .cp import Cp

def compactFloat(f: float) -> str:
    return ('%.3f' % f).rstrip('0').rstrip('.')

def to_svg(cp: Cp, margin=10) -> str:
    edgeSvg = ''
    mountainSvg = ''
    valleySvg = ''
    auxSvg = ''
    for line in cp.lines:
        lineSvg = "M{} {} L{} {}".format(compactFloat(line.x1), compactFloat(
            line.y1), compactFloat(line.x2), compactFloat(line.y2))
        if (line.type == 1):
            edgeSvg += lineSvg

        if (line.type == 2):
            mountainSvg += lineSvg

        if (line.type == 3):
            valleySvg += lineSvg

        if (line.type == 4):
            auxSvg += lineSvg

    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN" "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg version="1.0" xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="{v0} {v1} {v2} {v3}">
<path d="{edgePath}" stroke="black"/>
<path d="{mountainPath}" stroke="red"/>
<path d="{valleyPath}" stroke="blue"/>
<path d="{auxPath}" stroke="grey"/>
</svg>""".format(width=1024, height=1024, v0=compactFloat(cp.minX-margin), v1=compactFloat(cp.minY-margin), v2=compactFloat(cp.maxX-cp.minX+2*margin), v3=compactFloat(cp.maxY-cp.minY+2*margin), edgePath=edgeSvg, mountainPath=mountainSvg, valleyPath=valleySvg, auxPath=auxSvg)