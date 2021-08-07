from .from_opx import from_opx
from .to_svg import to_svg


def opx2svg(infile: str, outfile: str, margin=10):
    cp = from_opx(infile)

    svg_string = to_svg(cp, margin)

    with open(outfile, 'w') as im:
        im.write(svg_string)
