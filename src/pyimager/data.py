"""
pyimager.data
Submodule for pyimagers data

c - pycols.color object
reset - pycols.color.RESET_ALL code
b - pycols.Back object
cl - pycols.Back.BCLIST+pycols.Back.BLCLIST list
el - alphabetic list a - r
cols - None
"""
import pycols
c = pycols.color()
reset = c.RESET_ALL
b = pycols.Back()
cl = b.BCLIST+b.BLCLIST #initialize pycols color code elements
el = list("abcdefghijklmnopqr") #initialize list of lkim code elements
cols = None