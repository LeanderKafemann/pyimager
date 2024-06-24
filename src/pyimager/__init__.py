"""
PYIMAGER
funcs:
display -- displays image
compress -- compresses image file
decompress -- decompresses image file
compressor -- compresses whole file anew
about -- returns information about your release

Start pyimager to enter designer mode and create your own lkims!
"""
def about():
    """
    Returns information about your release and other projects by LK.
    """
    return {"Version":(3, 0, 2), "Author":"Leander Kafemann", "date":"24.6.2024", "recommend":("Büro by LK"), "feedbackTo": "leander@kafemann.berlin"}

import pycols, time
c = pycols.color()
reset = c.RESET_ALL
b = pycols.Back()
cl = b.BCLIST+b.BLCLIST
el = list("abcdefghijklmnopqr")
cols = None

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
    If target is left empty, the given file gets overwritten.
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
    If target is left empty, the given file is overwritten.
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
    If target is left empty, the given file is overwritten.
    """
    if target == "":
        target = path
    decompress(path, target)
    compress(target, target)
    
class Designer:
    def __init__(self):
        self.paletteText = "abcdefghijklmnopqr"
        self.paletteDisplay = "18#*#1#**#"+self.paletteText
        self.width = 0
        self.height = 0
        self.imTextSchabl = "{}#*#{}#**#{}"
        self.imText = ""
    def run_designer(self):
        print("Designer loading...")
        self.show_palette()
        finish = ""
        while finish == "":
            newRow = input("Enter new row of image: ")
            if self.width == 0:
                self.width = len(newRow)
            else:
                if len(newRow) != self.width:
                    self.raise_error("Invalid or inconsistent width")
            self.imText += newRow
            self.height += 1
            print("Current image:")
            display("display_content", self.imTextSchabl.format(str(self.width), str(self.height), self.imText))
            print("Image Data: Width: {} - Height: {}".format(str(self.width), str(self.height)))
            finish = input("Finish image? Enter anything to finish: ")
        if self.height == 0:
            self.raise_error("Invalid height (0)")
        imPath = input("Enter path to save image (.lkim file): ")
        with open(imPath, "w") as f:
            f.write(self.imTextSchabl.format(str(self.width), str(self.height), self.imText))
        print("Displaying new image...")
        display(imPath)
    def show_palette(self):
        display("display_content", self.paletteDisplay)
        print(self.paletteText)
    def raise_error(self, errorText: str = ""):
        quit(code=errorText)

if __name__ == "__main__":
    d = Designer()
    d.run_designer()
    input("Finish...")