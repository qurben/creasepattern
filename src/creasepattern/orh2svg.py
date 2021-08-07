from .from_orh import from_orh
from .to_svg import to_svg


def orh2svg(infile: str, outfile: str, margin=10):
    cp = from_orh(infile)

    svg_string = to_svg(cp, margin)

    with open(outfile, 'w') as im:
        im.write(svg_string)
