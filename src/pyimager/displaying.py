"""
pyimager.displaying
Submodule for displaying image

display -- displays image
"""
from .data import cl, el, reset
from .compressing import temp_uncompress

def display(path: str, display_content: str = ""):
    """
    Displays image of lkim-format in console.
    If the given sizes are invalid, an error is raised.
    If path is set to 'display_content', the content of display_content (e.g. content of a lkim) is displayed instead.
    """
    if path != "display_content":
        with open(path, "r") as f:
            sizes, data = f.read().split("#**#")
    else:
        sizes, data = display_content.split("#**#")
    WIDTH, HEIGHT = sizes.split("#*#")
    WIDTH = int(WIDTH); HEIGHT = int(HEIGHT)
    data = temp_uncompress(data, "$", 5)
    data = temp_uncompress(data, "%", 10)
    data = temp_uncompress(data, "&", 20)
    data = temp_uncompress(data, "§", 50)
    if WIDTH * HEIGHT != len(data) or WIDTH > 150 or HEIGHT > 100:
        print(WIDTH, HEIGHT, WIDTH*HEIGHT, len(data))
        print("Invalid image size.")
        raise ValueError("Invalid File")
    count = 1
    for i in data:
        if count < WIDTH:
            print(cl[el.index(i)]+" "+reset, end="")
        else:
            print(cl[el.index(i)]+" "+reset)
            count = 0
        count += 1
