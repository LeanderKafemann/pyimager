"""
Submodule for designer mode.
Enter !help during designer mode for more information.
"""

from .displaying import display
from .compressing import compress
from .message import errorMessageB

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
                case "!finish":
                    break
                case "!quit":
                    self.raise_error("You quitted Designer mode.", quit_=True)
                case "!show":
                    self.show_palette()
                case "!undo":
                    self.imText = self.imText[0:-1*self.width]
                    self.height -= 1
                case "!repeat":
                    self.imText += self.imText[-1*self.width if self.height != 1 else 0:]
                    self.height += 1
                case "!help" | "!command" | "command_" | "rowCode_":
                    print("Short description of Designer Mode", "For more information read the documentation or view the code", "",\
                          "Enter one of the following: rowCode_, !help, command_", "!help      - returns you here",\
                          "rowCode_   - a rowCode is the lkim content of a lkim row", 13*" "+"you have to enter the colors codes as seen above",\
                          "command_   - a command executes some helpful options", "commands are:",\
                          "!undo      - removes the last row placed", "!repeat    - adds the last placed row again",\
                          "!show      - shows the colors and their codes again",\
                          "!fill x    - fills the whole row with x-es, x is one or more signs of your choice,", 13*" "+"but len(x) must be a divisor of image width",\
                          "!finish    - saves the image", "!quit      - quits Designer mode", sep="\n")
                case _:
                    if not "!fill" in newRow:
                        print("Adding new row...")
                        if self.width == 0:
                            self.width = len(newRow)
                        else:
                            if len(newRow) != self.width:
                                self.raise_error("Invalid or inconsistent width")
                        self.imText += newRow
                        self.height += 1
                    else:
                        print("Filling new row...")
                        newR = newRow.split("!fill ")[-1]
                        newR_ = newR * int(self.width / len(newR))
                        if len(newR_) == 0:
                            self.raise_error("Invalid fill term")
                        self.imText += newR_
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
    def raise_error(self, errorText: str = "", quit_: bool = False):
        """
        Raises error
        """
        errorMessageB(errorText)
        if quit_:
            quit(code="quitted")
        else:
            self.__init__()
            self.run_designer()