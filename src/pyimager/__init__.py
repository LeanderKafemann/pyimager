"""
PYIMAGER
funcs:
display -- displays image
compress -- compresses image file
decompress -- decompresses image file
compressor -- compresses whole file anew
about -- returns information about your release

Start pyimager to enter designer mode and create your own lkims!

If pyimager is executed directly via cmd, __main__.py will be called.
This will also start designer mode.
"""
def about():
    """
    Returns information about your release and other projects by LK.
    """
    return {"Version":(3, 1, 0), "Author":"Leander Kafemann", "date":"24.6.2024", "recommend":("Büro by LK"), "feedbackTo": "leander@kafemann.berlin"}

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
    """
    Class for pyimagers Designer Mode.
    BETA function
    """
    def __init__(self):
        self.paletteText = "abcdefghijklmnopqr"
        self.paletteDisplay = "18#*#1#**#"+self.paletteText
        self.width = 0
        self.height = 0
        self.imTextSchabl = "{}#*#{}#**#{}"
        self.imText = ""
    def run_designer(self):
        """
        Runs Designer Mode
        """
        print("Designer loading...")
        self.show_palette()
        while True:
            print("Current image:")
            display("display_content", self.imTextSchabl.format(str(self.width), str(self.height), self.imText))
            print("Image Data: Width: {} - Height: {}".format(str(self.width), str(self.height)))
            newRow = input("Enter new row of image, command or help: ")
            if newRow == "finish":
                break
            elif newRow == "undo":
                self.imText = self.imText[0:-1*self.width]
                self.height -= 1
            elif newRow == "repeat":
                self.imText += self.imText[-1*self.width if self.height != 1 else 0:]
                self.height += 1
            elif newRow == "help":
                print("Short description of Designer Mode", "For more information read the documentation or view the code",\
                      "Enter one of the following: rowCode_, help, command_", "help", "help returns you here",\
                      "rowCode_", "a rowCode is the lkim content of a lkim row", "you have to enter the colors codes as seen above",\
                      "command_", "a command will execute some helpful options so you save time",\
                      "undo removes the last row placed", "repeat addes the last row again", sep="\n")
            else:
                print("Adding new row...")
                if self.width == 0:
                    self.width = len(newRow)
                else:
                    if len(newRow) != self.width:
                        self.raise_error("Invalid or inconsistent width")
                self.imText += newRow
                self.height += 1
        if self.height == 0:
            self.raise_error("Invalid height (0)")
        imPath = input("Enter path to save image (.lkim file): ")
        with open(imPath, "w") as f:
            f.write(self.imTextSchabl.format(str(self.width), str(self.height), self.imText))
        compress(imPath)
        print("Displaying new image...")
        display(imPath)
    def show_palette(self):
        """
        Shows available colors and codes
        """
        display("display_content", self.paletteDisplay)
        print(self.paletteText)
    def raise_error(self, errorText: str = ""):
        """
        Raises error
        """
        quit(code=errorText)

if __name__ == "__main__":
    d = Designer()
    d.run_designer()
    input("Finish...")