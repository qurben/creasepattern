from .to_png import to_png
from .from_cp import from_cp

def cp2png(infile, outfile, size=2048, margin=20, aa_scale=4):
    cp = from_cp(infile)

    im = to_png(cp, size, margin, aa_scale)

    im.save(outfile, 'PNG')
