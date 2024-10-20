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
        with open(path, "r", encoding="utf-8") as f:
            sizes, data_ = f.read().split("#**#")
    else:
        sizes, data_ = display_content.split("#**#")
    WIDTH, HEIGHT = sizes.split("#*#")
    WIDTH = int(WIDTH); HEIGHT = int(HEIGHT)
    data_ = temp_uncompress(data_, "$", 5)
    data_ = temp_uncompress(data_, "%", 10)
    data_ = temp_uncompress(data_, "&", 20)
    data_ = temp_uncompress(data_, "§", 50)
    if WIDTH * HEIGHT != len(data_) or WIDTH > 150 or HEIGHT > 100:
        print(WIDTH, HEIGHT, WIDTH*HEIGHT, len(data_))
        print("Invalid image size.")
        raise ValueError("Invalid File")
    count = 1
    for i in data_:
        if count < WIDTH:
            print(cl[el.index(i)]+" "+reset, end="")
        else:
            print(cl[el.index(i)]+" "+reset)
            count = 0
        count += 1
