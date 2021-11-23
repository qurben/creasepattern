import os
import sys

from creasepattern import cp2png, cp2svg, opx2png, orh2png, orh2svg, opx2svg, orh2cp, opx2cp


def main():
    if len(sys.argv) != 3:
        print("""Usage:
        {0} creasepattern.cp image.png
        {0} creasepattern.cp image.svg""".format(os.path.basename(sys.argv[0])))
        exit()

    infile = sys.argv[1]
    outfile = sys.argv[2]

    conversion_map = {
        '.opx.png': opx2png,
        '.opx.svg': opx2svg,
        '.opx.cp': opx2cp,
        '.orh.png': orh2png,
        '.orh.svg': orh2svg,
        '.orh.cp': orh2cp,
        '.cp.png': cp2png,
        '.cp.svg': cp2svg,
    }

    _, in_file_extension = os.path.splitext(infile)
    _, out_file_extension = os.path.splitext(outfile)

    key = in_file_extension + out_file_extension

    if key in conversion_map:
        conversion_map[key](infile, outfile)


if __name__ == '__main__':
    main()
