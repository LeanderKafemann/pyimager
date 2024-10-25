"""
Submodule for sending colorated messages.
"""
from .data import c

def errorMessageB(message: str = "An error occured.", errorCol: str = "RED"):
    """
    Sends error message with red background.
    """
    print(c.bcol(errorCol) + message + c.bcol("RESET"))

def errorMessage(message: str = "An error occured.", errorCol: str = "RED"):
    """
    Sends error message with red text.
    """
    print(c.col(errorCol) + message + c.col("RESET"))