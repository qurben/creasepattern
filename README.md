# creasepattern

Basic tools to work with Origami Crease Patterns.

## Usage

Install with pip

```
pip install creasepattern
```

This installs the `crease` executable:

```
Usage:
        crease creasepattern.cp image.png
        crease creasepattern.cp image.svg
```

### `cp2png(infile, outfile, size=2048, margin=20, aa_scale=4)`

Convert `.cp` files to `.png`

Size of the output file is scaled to the given size, either horizonally or vertically, whichever is larger.

`aa_scale` is used to anti alias. Set to 1 to disable anti aliasing.

```python
from creasepattern import cp2png

cp2png('file.cp', 'file.png')
```

### `cp2svg(infile, outfile, margin=10)`

Convert `.cp` files to `.svg`

```python
from creasepattern import cp2svg

cp2svg('file.cp', 'file.svg')
```

### `opx2png(infile, outfile, size=2048, margin=20, aa_scale=4)`

Convert Oripa `.opx` to `.png`

### `opx2svg(infile, outfile, margin=10)`

Convert Oripa `.opx` to `.svg`

### `opx2cp(infile, outfile)`

Convert Oripa `.opx` to `.cp`

### `orh2png(infile, outfile, size=2048, margin=20, aa_scale=4)`

Convert Orihime `.orh` to `.png`

### `orh2svg(infile, outfile, margin=10)`

Convert Orihime `.orh` to `.svg`.

Only supports exporting normal lines, so no folded bases, aux circles and non-interfering aux lines.

### `orh2cp(infile, outfile)`

Convert Orihime `.orh` to `.cp`.

### `from_cp(infile: str) -> Cp`

Convert `.cp` to a `Cp` object.

### `from_cp_str(lines: list[str]) -> Cp`

Convert string lines in `.cp` format to a `Cp` object.

### `from_opx(infile: str) -> Cp`

Convert Oripa `.opx` to a `Cp` object.

### `from_orh(infile: str) -> Cp`

Convert Orihime `.orh` to a `Cp` object

### `to_svg(cp: Cp) -> str`

Convert a `Cp` object to an svg string

### `to_png(cp: Cp) -> Image`

Convert a `Cp` object to a PIL Image

### `to_cp`(cp : Cp) -> str`

Convert a `Cp` object to a `.cp` file string.

## Roadmap

* (Must) Make size of output configurable
* (Must) Make edge types configurable
* (Could) Support more filetypes