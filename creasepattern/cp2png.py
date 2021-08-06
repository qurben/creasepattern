from .cp import Cp

from PIL import Image, ImageDraw

factor = 8

margin = 20

def cp2png(infile, outfile):
    cp = Cp(infile)

    width, height = cp.size()

    with Image.new('RGB', (width * factor + 2 * margin, height * factor + 2 * margin)) as im:
        draw = ImageDraw.Draw(im)

        # Fill background
        draw.rectangle([0, 0, width * factor + 2 * margin, height * factor + 2 * margin],
                       fill=(255, 255, 255))

        for line in cp.lines:
            draw.line((((line.x1 - cp.minX) * factor) + margin, ((line.y1 - cp.minY) * factor) + margin,
                       ((line.x2 - cp.minX) * factor) + margin, ((line.y2 - cp.minY) * factor) + margin), fill=line.color(), width=2)

        # Apply anti alias
        im = im.resize(
            ((width * factor + (2 * margin)) // 2, (height * factor + (2 * margin)) // 2), resample=Image.ANTIALIAS)

        im.save(outfile, "PNG")

if __name__ == '__main__':
    cp2png('snek2.cp', 'snek2.png')
