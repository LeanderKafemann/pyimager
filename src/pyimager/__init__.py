"""
PYIMAGER
funcs:
display -- displays image
"""
def about():
    """
    Returns information about your release and other projects by LK
    """
    return {"Version":(1, 0, 0), "Author":"Leander Kafemann", date:"30.12.2023", recommend:("Büro by LK", "Verschlüsseler by LK", "flappy bird by LK", "naturalsize by LK"), feedbackTo: "leander@kafemann.berlin"}

import pycols
c = pycols.color()
reset = c.RESET_ALL
b = pycols.Back()
cl = b.BCLIST+b.BLCLIST
el = list("abcdefghijklmnopqrst")

def display(path: str):
    """
    Displays image of lkim-format in console.
    When the given sizes are invalid, an error is raised.
    """
    with open(path, "r") as f:
        sizes, data = f.read().split("#**#")
    WIDTH, HEIGHT = sizes.split("#*#")
    WIDTH = int(WIDTH); HEIGHT = int(HEIGHT)
    if WIDTH * HEIGHT != len(data) or WIDTH > 150 or HEIGHT > 100:
        raise ValueError("Invalid File")
    count = 1
    for i in data:
        if count < WIDTH:
            print(cl[el.index(i)]+" "+reset, end="")
        else:
            print(cl[el.index(i)]+" "+reset)
            count = 0
        count += 1
