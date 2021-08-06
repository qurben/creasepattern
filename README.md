# creasepattern

Basic topls to work with Origami Crease Patterns.

## Usage

### cp2png

Convert `.cp` files to `.png`

Size of the output image is based on the sizes given in the `.cp` file.

```python
from creasepattern import cp2png

cp2png('file.cp', 'file.png')
```

### cp2svg

Convert `.cp` files to `.svg`

```python
from creasepattern import cp2svg

cp2png('file.cp', 'file.svg')
```

## Roadmap

* (Must) Make size of output configurable
* (Must) Make edge types configurable
* (Could) Support more filetypes