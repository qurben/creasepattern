from creasepattern import cp2png, cp2svg
import sys

if len(sys.argv) != 4:
    print("""Usage:
{0} png creasepattern.cp image.png
{0} svg creasepattern.cp image.svg""".format(sys.argv[0]))
    exit()

if sys.argv[1] == 'svg':
    cp2svg(sys.argv[2], sys.argv[3])
if sys.argv[1] == 'png':
    cp2png(sys.argv[2], sys.argv[3])
