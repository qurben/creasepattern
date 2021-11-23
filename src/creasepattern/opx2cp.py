from .from_opx import from_opx
from .to_cp import to_cp


def opx2cp(infile: str, outfile: str):
    cp = from_opx(infile)

    cp_string = to_cp(cp)

    with open(outfile, 'w') as im:
        im.write(cp_string)
