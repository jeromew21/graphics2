# graphics2.py

Being a big fan of clean APIs and good abstraction, [graphics.py](http://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf) is one of my favorite tools if I need a quick and dirty GUI for Python.

## Motivation

Graphics is *lovely*, but can be lacking in performance (it uses Tkinter as a backend). graphics2 uses [pygame](https://www.pygame.org/news) instead.

## Usage

### Just swap in graphics2 wherever you use graphics

The API is completely compatible (will be when this is completed), so you can simply drop this file in your project and import it instead.

### Installation

Requires [pygame](https://www.pygame.org/news)

```
pip install pygame
```

Tested in Python 3.6

## Additional features

- Set icon

## Drawbacks

- Pygame dependency. Pygame is a somewhat heavy library and pulls dependencies itself.
- Font rendering is somewhat inferior.
- Slow startup time

## Documentation

See original documentation [here](http://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf). TODO: Document extra features.
