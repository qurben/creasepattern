from .from_opx import from_opx
from .to_svg import to_svg

def opx2svg(infile, outfile, margin=10):
    cp = from_opx(infile)

    svgString = to_svg(cp, margin)
    
    with open(outfile, 'w') as im:
        im.write(svgString)
