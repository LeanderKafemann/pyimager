"""
PYIMAGER
funcs:
display -- displays image
compress -- compresses image file
decompress -- decompresses image file
compressor -- compresses whole file anew
temp_uncompress -- uncompresses lkim-data temporarily
about -- returns information about your release

Start pyimager via cmd to execute __main__.py,
which will make you enter the Designer Mode to create your own lkims.
"""
def about():
    """
    Returns information about your release and other projects by LK.
    """
    return {"Version":(3, 3, 1), "Author":"Leander Kafemann", "date":"07.08.2024", "recommend":("Büro by LK"), "feedbackTo": "leander@kafemann.berlin"}

import pycols
c = pycols.color()
reset = c.RESET_ALL
b = pycols.Back()
cl = b.BCLIST+b.BLCLIST #initialize pycols color code elements
el = list("abcdefghijklmnopqr") #initialize list of lkim code elements
cols = None

comb1 = el.copy()
comb2 = []
for i in el:
    for j in el:
        if i != j:
            comb2.append(i+j)
comb3 = []
for i in el:
    for j in el:
        for k in el:
            if i != j and i != k and j != k:
                comb3.append(i+j+k)
combList = comb3+comb2+comb1 #initialize list of possible combinations of lkim code elements
#todo:
#4-er Liste aus 2-er Liste zusammensetzen usw.              

def temp_uncompress(data: str, sgn: str, sgn_codec: int):
    """
    Uncompresses content of data, but only uncompresses codecs with given sign.
    Replaces it by sgn_codec times the content of the compression matrix.
    """
    sgn_found = []
    for i in range(len(data)):
        if data[i] == sgn:
            sgn_found.append(i)
    sgn_found_tpl = []
    for i in range(int(len(sgn_found)/2)):
        sgn_found_tpl += [(sgn_found[2*i], sgn_found[2*i+1])]
    if len(sgn_found_tpl) == 0:
        return data
    betw = data[sgn_found_tpl[0][0]+1:sgn_found_tpl[0][1]]
    data_new = data[:sgn_found_tpl[0][0]] + sgn_codec*betw
    sgn_found_tpl.pop(0)
    for i in sgn_found_tpl:
        betw = data[i[0]+1:i[1]]
        idx = sgn_found.index(i[0]) - 1
        data_new += data[sgn_found[idx]+1:i[0]] + sgn_codec*betw
    data_new += data[sgn_found[-1]+1:]
    return data_new

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

def compress(path: str, target: str = ""):
    """
    Compresses LKIM with replacing frequent pixels.
    If target is left empty, the given file gets overwritten.
    """
    with open(path, "r", encoding="utf-8") as f:
        im = f.read()
    for i in combList:
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
    sizes, data = im.split("#**#")
    data = temp_uncompress(data, "$", 5)
    data = temp_uncompress(data, "%", 10)
    data = temp_uncompress(data, "&", 20)
    data = temp_uncompress(data, "§", 50)
    if target == "":
        target = path
    with open(target, "w", encoding="utf-8") as f:
        f.write(sizes+"#**#"+data)

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
            elif newRow == "help" or newRow == "command":
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
