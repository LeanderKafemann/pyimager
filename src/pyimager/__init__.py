"""
PYIMAGER
Module for displaying images in console

submodules:
pyimager.designer -- submodule of Designer mode
pyimager.display -- submodule for displaying images
pyimager.compress -- submodule for compressing images
pyimager.utils -- pyimagers utils
pyimager.data -- pyimagers data

Start pyimager via cmd to execute __main__.py,
which will make you enter the Designer Mode to create your own lkims.
"""
def about():
    """
    Returns information about your release and other projects by LK.
    """
    return {"version": (3, 4, 1), "author": "Leander Kafemann", "date": "19.08.2024", "recommend": ("Büro by LK"), "feedback to": "leander@kafemann.berlin"}

from . import utils
from . import compress
from . import display
from . import designer
from . import data

from .display import *
from .designer import *
from .compress import *
from .data import *
