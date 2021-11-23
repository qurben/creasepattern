from .from_orh import from_orh
from .to_cp import to_cp


def orh2cp(infile: str, outfile: str):
    cp = from_orh(infile)

    cp_string = to_cp(cp)

    with open(outfile, 'w') as im:
        im.write(cp_string)
