from .from_opx import from_opx
from .to_png import to_png


def opx2png(infile: str, outfile: str, size=2048, margin=20, aa_scale=4) -> None:
    cp = from_opx(infile)

    im = to_png(cp, size, margin, aa_scale)

    im.save(outfile, 'PNG')
