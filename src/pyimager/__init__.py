"""
PYIMAGER
Module for displaying images in console

submodules:
pyimager.designer -- submodule of Designer mode
pyimager.displaying -- submodule for displaying images
pyimager.compressing -- submodule for compressing images
pyimager.utils -- pyimagers utils
pyimager.data -- pyimagers data

Start pyimager via cmd to execute __main__.py,
which will make you enter the Designer Mode to create your own lkims.
"""
def about():
    """
    Returns information about your release and other projects by LK.
    """
    return {"version": (3, 4, 3), "author": "Leander Kafemann", "date": "3.10.2024", "recommend": ("Büro by LK"), "feedback to": "leander@kafemann.berlin"}

from . import utils
from . import compressing
from . import displaying
from . import designer
from . import data

from .displaying import *
from .designer import *
from .compressing import *
from .data import *
