"""
PYIMAGER
funcs:
display -- displays image
compress -- compresses image file
decompress -- decompresses image file
compressor -- compresses whole file anew
about -- returns information about your release
"""
def about():
    """
    Returns information about your release and other projects by LK
    """
    return {"Version":(2, 0, 2), "Author":"Leander Kafemann", date:"20.3.2024", recommend:("Büro by LK", "Verschlüsseler by LK", "naturalsize by LK"), feedbackTo: "leander@kafemann.berlin"}

import pycols, time
c = pycols.color()
reset = c.RESET_ALL
b = pycols.Back()
cl = b.BCLIST+b.BLCLIST
el = list("abcdefghijklmnopqr")
cols = None

def display(path: str):
    """
    Displays image of lkim-format in console.
    When the given sizes are invalid, an error is raised.
    """
    with open(path, "r") as f:
        sizes, data = f.read().split("#**#")
    WIDTH, HEIGHT = sizes.split("#*#")
    WIDTH = int(WIDTH); HEIGHT = int(HEIGHT)
    for i in el:
        data = data.replace(f"%{i}%", i*10)
        data = data.replace(f"&{i}&", i*20)
        data = data.replace(f"${i}$", i*5)
        data = data.replace(f"§{i}§", i*50)
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

def compress(path: str, target: str = ""):
    """
    Compresses LKIM with replacing frequent pixels.
    When target is left empty, the given file gets overwritten.
    """
    with open(path, "r", encoding="utf-8") as f:
        im = f.read()
    for i in el:
        im = im.replace(i*50, f"§{i}§")
        im = im.replace(i*20, f"&{i}&")
        im = im.replace(i*10, f"%{i}%")
        im = im.replace(i*5, f"${i}$")
    if target == "":
        target = path
    with open(target, "w", encoding="utf-8") as f:
        f.write(im)

def decompress(path: str, target: str = ""):
    """
    Decompresses LKIM with replacing frequent pixels.
    When target is left empty, the given file is overwritten.
    """
    with open(path, "r", encoding="utf-8") as f:
        im = f.read()
    for i in el:
        im = im.replace(f"§{i}§", i*50)
        im = im.replace(f"&{i}&", i*20)
        im = im.replace(f"%{i}%", i*10)
        im = im.replace(f"${i}$", i*5)
    if target == "":
        target = path
    with open(target, "w", encoding="utf-8") as f:
        f.write(im)

def compressor(path: str, target: str = ""):
    """
    Decompresses and then compresses LKIM anew.
    When target is left empty, the given file is overwritten.
    """
    if target == "":
        target = path
    decompress(path, target)
    compress(target, target)

if __name__ == "__main__":
    print("Test erfolgreich abgeschlossen."); time.sleep(3)