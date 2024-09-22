from pygame.locals import KEYDOWN
from calculatorstuffs.buttons import *

class Console():
    def __init__(self):
        super().__init__()
        self.consoleText = ""
        self.text_pos = (59,192)
        self.buttons = {
            0: self.skip,
            1: self.yEquals,
            2: self.windowButton,
            3: self.zoomButton,
            4: self.traceButton,
            5: self.graphButton,
            6: self.secondButton,
            7: self.modeButton,
            8: self.delButton,
            9: self.alphaButton,
            10: self.xButton,
            11: self.statButton,
            12: self.mathButton,
            13: self.appsButton,
            14: self.prgmButton,
            15: self.varsButton,
            16: self.clearButton,
            17: self.xToPowerMinusOneButton,
            18: self.sinButton,
            19: self.cosButton,
            20: self.tanButton,
            21: self.xToPowerOfButton,
            22: self.xToPower2Button,
            23: self.commaButton,
            24: self.openParenthesisButton,
            25: self.closeParenthesisButton,
            26: self.divisionButton,
            27: self.logButton,
            28: self.sevenButton,
            29: self.eightButton,
            30: self.nineButton,
            31: self.multiplicationButton,
            32: self.lnButton,
            33: self.fourButton,
            34: self.fiveButton,
            35: self.sixButton,
            36: self.minusButton,
            37: self.stoButton,
            38: self.oneButton,
            39: self.twoButton,
            40: self.threeButton,
            41: self.plusButton,
            42: self.onButton,
            43: self.zeroButton,
            44: self.dotButton,
            45: self.negativeButton,
            46: self.enterButton,
            47: self.leftButton,
            48: self.rightButton,
            49: self.upButton,
            50: self.downButton
        }
    def update(self, value):
        self.button = self.buttons.get(value)
        self.button()
    def skip(self):
        pass
    def yEquals(self):
        print("no")
    def windowButton(self):
        print("no")
    def zoomButton(self):
        print("no")
    def traceButton(self):
        print("no")
    def graphButton(self):
        print("no")
    def secondButton(self):
        print("no")
    def modeButton(self):
        print("no")
    def delButton(self):
        print("no")
    def alphaButton(self):
        print("no")
    def xButton(self):
        print("no")
    def statButton(self):
        print("no")
    def mathButton(self):
        print("no")
    def appsButton(self):
        print("no")
    def prgmButton(self):
        print("no")
    def varsButton(self):
        print("no")
    def clearButton(self):
        print("no")
    def xToPowerMinusOneButton(self):
        print("no")
    def sinButton(self):
        print("no")
    def cosButton(self):
        print("no")
    def tanButton(self):
        print("no")
    def xToPowerOfButton(self):
        print("no")
    def xToPower2Button(self):
        print("no")
    def commaButton(self):
        print("no")
    def openParenthesisButton(self):
        print("no")
    def closeParenthesisButton(self):
        print("no")
    def divisionButton(self):
        print("no")
    def logButton(self):
        print("no")
    def sevenButton(self):
        self.consoleText += "7"
    def eightButton(self):
        self.consoleText += "8"
    def nineButton(self):
        self.consoleText += "9"
    def multiplicationButton(self):
        print("no")
    def lnButton(self):
        print("no")
    def fourButton(self):
        self.consoleText += "4"
    def fiveButton(self):
        self.consoleText += "5"
    def sixButton(self):
        self.consoleText += "6"
    def minusButton(self):
        print("no")
    def stoButton(self):
        print("no")
    def oneButton(self):
        self.consoleText += "1"
    def twoButton(self):
        self.consoleText += "2"
    def threeButton(self):
        self.consoleText += "3"
    def plusButton(self):
        print("no")
    def onButton(self):
        print("no")
    def zeroButton(self):
        self.consoleText += "0"
    def dotButton(self):
        print("no")
    def negativeButton(self):
        print("no")
    def enterButton(self):
        print("no")
    def leftButton(self):
        print("no")
    def rightButton(self):
        print("no")
    def upButton(self):
        print("no")
    def downButton(self):
        print("no")
    def draw(self):
        text(self.text_pos, self.consoleText)

# points1 = [
#     (59, 189, 80, 211)
#     (249, 159, 262, 181)
# ]