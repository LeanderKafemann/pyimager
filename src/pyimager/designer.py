from .displaying import display
from .compressing import compress

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
            match newRow:
                case "finish":
                    break
                case "undo":
                    self.imText = self.imText[0:-1*self.width]
                    self.height -= 1
                case "repeat":
                    self.imText += self.imText[-1*self.width if self.height != 1 else 0:]
                    self.height += 1
                case "help" | "command":
                    print("Short description of Designer Mode", "For more information read the documentation or view the code",\
                          "Enter one of the following: rowCode_, help, command_", "help", "help returns you here",\
                          "rowCode_", "a rowCode is the lkim content of a lkim row", "you have to enter the colors codes as seen above",\
                          "command_", "a command will execute some helpful options so you save time",\
                          "undo removes the last row placed", "repeat addes the last row again",\
                          "finish saves the image", sep="\n")
                case _:
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
        print("Compressing image...")
        compress(imPath, includeComb6=True)
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