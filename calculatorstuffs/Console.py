from pygame.locals import KEYDOWN
from calculatorstuffs.buttons import *
import math as meth

class Console():
    def __init__(self):
        super().__init__()
        self.consoleText = ""
        self.consoleCharacter = ""
        self.evalText = ""
        self.consoleLog = []
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
        self.home_screen = pygame.image.load('calculatorstuffs/assets/ti-84boxesempty.png')
        self.home_screen = pygame.transform.smoothscale(self.home_screen, (320, 720))
        self.screen = pygame.image.load('calculatorstuffs/assets/ti-84screen.png')
        self.screen = pygame.transform.smoothscale(self.screen, (220, 390))
    def update(self, value):
        self.button = self.buttons.get(value)
        self.button()
        self.consoleText += self.consoleCharacter
    def skip(self):
        self.notImplemented()
    def yEquals(self):
        self.notImplemented()
    def windowButton(self):
        self.notImplemented()
    def zoomButton(self):
        self.notImplemented()
    def traceButton(self):
        self.notImplemented()
    def graphButton(self):
        self.notImplemented()
    def secondButton(self):
        self.notImplemented()
    def modeButton(self):
        self.notImplemented()
    def delButton(self):
        self.notImplemented()
    def alphaButton(self):
        self.notImplemented()
    def xButton(self):
        self.notImplemented()
    def statButton(self):
        self.notImplemented()
    def mathButton(self):
        self.notImplemented()
    def appsButton(self):
        self.notImplemented()
    def prgmButton(self):
        self.notImplemented()
    def varsButton(self):
        self.notImplemented()
    def clearButton(self):
        self.consoleText = ""
        self.consoleCharacter = ""
        self.evalText = ""
    def xToPowerMinusOneButton(self):
        self.notImplemented()
    def sinButton(self):
        self.notImplemented()
    def cosButton(self):
        self.notImplemented()
    def tanButton(self):
        self.notImplemented()
    def xToPowerOfButton(self):
        self.notImplemented()
    def xToPower2Button(self):
        self.notImplemented()
    def commaButton(self):
        self.notImplemented()
    def openParenthesisButton(self):
        self.notImplemented()
    def closeParenthesisButton(self):
        self.notImplemented()
    def divisionButton(self):
        self.consoleCharacter = "/"
        self.evalText += "/"
    def logButton(self):
        self.notImplemented()
    def sevenButton(self):
        self.consoleCharacter = "7"
        self.evalText += "7"
    def eightButton(self):
        self.consoleCharacter = "8"
        self.evalText += "8"
    def nineButton(self):
        self.consoleCharacter = "9"
        self.evalText += "9"
    def multiplicationButton(self):
        self.consoleCharacter = "*"
        self.evalText += "*"
    def lnButton(self):
        self.notImplemented()
    def fourButton(self):
        self.consoleCharacter = "4"
        self.evalText += "4"
    def fiveButton(self):
        self.consoleCharacter = "5"
        self.evalText += "5"
    def sixButton(self):
        self.consoleCharacter = "6"
        self.evalText += "6"
    def minusButton(self):
        self.consoleCharacter = "-"
        self.evalText += "-"
    def stoButton(self):
        self.notImplemented()
    def oneButton(self):
        self.consoleCharacter = "1"
        self.evalText += "1"
    def twoButton(self):
        self.consoleCharacter = "2"
        self.evalText += "2"
    def threeButton(self):
        self.consoleCharacter = "3"
        self.evalText += "3"
    def plusButton(self):
        self.consoleCharacter = "+"
        self.evalText += "+"
    def onButton(self):
        self.notImplemented()
    def zeroButton(self):
        self.consoleCharacter = "0"
        self.evalText += "0"
    def dotButton(self):
        self.notImplemented()
    def negativeButton(self):
        self.notImplemented()
    def enterButton(self):
        self.consoleLog.insert(0, self.consoleText)
        self.consoleLog.insert(0, str(self.runConsoleText()))
        self.consoleCharacter = ""
        self.evalText = ""
        print(self.consoleLog)
    def leftButton(self):
        self.notImplemented()
    def rightButton(self):
        self.notImplemented()
    def upButton(self):
        self.notImplemented()
    def downButton(self):
        self.notImplemented()
    def notImplemented(self):
        print("no")
        self.consoleCharacter = ""
    def runConsoleText(self):
        if self.evalText != "":
            try:
                print(eval(self.consoleText))
                return eval(self.consoleText)
            except Exception as e:
                print(e)

    def draw(self, surf):
        surf.blit(self.screen, (52, 52))
        text(self.text_pos, self.consoleText)
        self.x, self.y = self.text_pos
        self.mod2 = 1
        for i in self.consoleLog:
            self.y -= 15
            if self.mod2 == 1:
                self.xOffset = 200
                text((self.x + self.xOffset, self.y), i, True)
            else:
                self.xOffset = 0
                text((self.x, self.y), i)
            self.mod2 *= -1
            # text((self.x + self.xOffset, self.y), i)

        surf.blit(self.home_screen, (0, 0))

# points1 = [
#     (59, 189, 80, 211)
#     (249, 159, 262, 181)
# ]