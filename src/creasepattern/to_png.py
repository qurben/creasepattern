import math
from PIL import Image, ImageDraw
from .cp import Cp


def to_png(cp: Cp, size=2048, margin=20, aa_scale=4) -> Image:
    width, height = cp.size()

    if width < height:
        factor = size * aa_scale / height
    else:
        factor = size * aa_scale / width

    # Calculate scale factor for lines within the margin
    if width < height:
        innerFactor = (size - margin * 2) * aa_scale / height
    else:
        innerFactor = (size - margin * 2) * aa_scale / width

    with Image.new('RGB', (math.ceil(width * factor), math.ceil(height * factor))) as im:
        draw = ImageDraw.Draw(im)

        # Fill background
        draw.rectangle([0, 0, width * factor, height * factor],
                       fill=(255, 255, 255))

        for line in cp.lines:
            draw.line((((line.x1 - cp.minX) * innerFactor) + margin * aa_scale, ((line.y1 - cp.minY) * innerFactor) + margin * aa_scale,
                       ((line.x2 - cp.minX) * innerFactor) + margin * aa_scale, ((line.y2 - cp.minY) * innerFactor) + margin * aa_scale), fill=line.color(), width=aa_scale)

        # Apply anti alias
        im = im.resize(
            (math.ceil((width * factor) // aa_scale), math.ceil((height * factor) // aa_scale)), resample=Image.ANTIALIAS)

        return im
