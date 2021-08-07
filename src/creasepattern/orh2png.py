from .from_orh import from_orh
from .to_png import to_png


def orh2png(infile: str, outfile: str, size=1024, margin=20, aa_scale=4) -> None:
    cp = from_orh(infile)

    im = to_png(cp, size, margin, aa_scale)

    im.save(outfile, 'PNG')
