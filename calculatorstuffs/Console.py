from pygame.locals import KEYDOWN
from calculatorstuffs.buttons import *
import math as meth
import time

class Console():
    def __init__(self):
        super().__init__()
        self.consoleText = ""
        self.consoleCharacter = ""
        self.evalText = ""
        self.evalCharacter = ""
        self.consoleLog = []
        self.text_pos = (59,192)
        self.highlight_pos = [60, 192]
        self.highlightDimensions = ()
        self.time = 0
        self.timeBlinked = 0
        self.blink = True
        self.acceptingInput = True
        self.keyAttribute = 0
        self.ans = None
        self.alphaLock = False
        self.buttons = {
            0: self.skip,
            1: self.yEqualsButton,
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
            50: self.downButton,
            (0, 0, 0, 48): self.zeroButton,
            (0, 0, 0, 49): self.oneButton,
            (0, 0, 0, 50): self.twoButton,
            (0, 0, 0, 51): self.threeButton,
            (0, 0, 0, 52): self.fourButton,
            (0, 0, 0, 53): self.fiveButton,
            (0, 0, 0, 54): self.sixButton,
            (0, 0, 0, 55): self.sevenButton,
            (0, 0, 0, 56): self.eightButton,
            (0, 0, 0, 57): self.nineButton,
            (1, 0, 0, 61): self.plusButton,
            (0, 0, 0, 45): self.minusButton,
            (1, 0, 0, 56): self.multiplicationButton,
            (0, 0, 0, 47): self.divisionButton,
            (0, 0, 0, 13): self.enterButton,
            (1, 0, 0, 57): self.openParenthesisButton,
            (1, 0, 0, 48): self.closeParenthesisButton,
        }
        self.home_screen = pygame.image.load('calculatorstuffs/assets/ti-84boxesempty.png')
        self.home_screen = pygame.transform.smoothscale(self.home_screen, (320, 720))
        self.screen = pygame.image.load('calculatorstuffs/assets/ti-84screen.png')
        self.screen = pygame.transform.smoothscale(self.screen, (220, 390))
    def update(self, value):
        self.button = self.buttons.get(value)
        if self.button != None:
            self.button(self.keyAttribute)
            self.consoleText += self.consoleCharacter
            self.evalText += self.evalCharacter
            self.consoleCharacter = ""
            self.evalCharacter = ""
            if self.keyAttribute != 0:
                if self.keyAttribute == 1:
                    if value != 6:
                        self.keyAttribute = 0
                elif self.keyAttribute == 2:
                    if value != 9 and not self.alphaLock:
                        self.keyAttribute = 0           
    def skip(self, keyAttribute):
        pass
    def yEqualsButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def windowButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def zoomButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def traceButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def graphButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def secondButton(self, keyAttribute):
        if keyAttribute == 0:
            self.keyAttribute = 1
        if keyAttribute == 1:
            self.keyAttribute = 0
        if keyAttribute == 2:
            self.keyAttribute = 1
    def modeButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def delButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def alphaButton(self, keyAttribute):
        if keyAttribute == 0:
            self.keyAttribute = 2
        if keyAttribute == 1:
            self.keyAttribute = 2
            self.alphaLock = True
        if keyAttribute == 2:
            self.keyAttribute = 0
            self.alphaLock = False
    def xButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def statButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def mathButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def appsButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def prgmButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def varsButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def clearButton(self, keyAttribute):
        if keyAttribute == 0:
            if self.acceptingInput:
                self.consoleText = ""
                self.consoleCharacter = ""
                self.evalText = ""
                self.highlight_pos = [60, 192]
    def xToPowerMinusOneButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def sinButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def cosButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def tanButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def xToPowerOfButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def xToPower2Button(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def commaButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def openParenthesisButton(self, keyAttribute):
        if keyAttribute == 0:
            self.consoleCharacter = "("
            self.evalCharacter = "("
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def closeParenthesisButton(self, keyAttribute):
        if keyAttribute == 0:
            self.consoleCharacter = ")"
            self.evalCharacter = ")"
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def divisionButton(self, keyAttribute):
        if keyAttribute == 0:
            if self.consoleText == "":
                self.consoleCharacter = "Ans/"
                self.evalCharacter = f"{self.ans}/"
                return
            self.consoleCharacter = "/"
            self.evalCharacter = "/"
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def logButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def sevenButton(self, keyAttribute):
        if keyAttribute == 0:
            self.consoleCharacter = "7"
            self.evalCharacter = "7"
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def eightButton(self, keyAttribute):
        if keyAttribute == 0:
            self.consoleCharacter = "8"
            self.evalCharacter = "8"
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def nineButton(self, keyAttribute):
        if keyAttribute == 0:
            self.consoleCharacter = "9"
            self.evalCharacter = "9"
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def multiplicationButton(self, keyAttribute):
        if keyAttribute == 0:
            if self.consoleText == "":
                self.consoleCharacter = "Ans*"
                self.evalCharacter = f"{self.ans}*"
                return
            self.consoleCharacter = "*"
            self.evalCharacter = "*"
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def lnButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def fourButton(self, keyAttribute):
        if keyAttribute == 0:
            self.consoleCharacter = "4"
            self.evalCharacter = "4"
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def fiveButton(self, keyAttribute):
        if keyAttribute == 0:
            self.consoleCharacter = "5"
            self.evalCharacter = "5"
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def sixButton(self, keyAttribute):
        if keyAttribute == 0:
            self.consoleCharacter = "6"
            self.evalCharacter = "6"
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def minusButton(self, keyAttribute):
        if keyAttribute == 0:
            if self.consoleText == "":
                self.consoleCharacter = "Ans-"
                self.evalCharacter = f"{self.ans}-"
                return
            self.consoleCharacter = "-"
            self.evalCharacter = "-"
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def stoButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def oneButton(self, keyAttribute):
        if keyAttribute == 0:
            self.consoleCharacter = "1"
            self.evalCharacter = "1"
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def twoButton(self, keyAttribute):
        if keyAttribute == 0:
            self.consoleCharacter = "2"
            self.evalCharacter = "2"
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def threeButton(self, keyAttribute):
        if keyAttribute == 0:
            self.consoleCharacter = "3"
            self.evalCharacter = "3"
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def plusButton(self, keyAttribute):
        if keyAttribute == 0:
            if self.consoleText == "":
                self.consoleCharacter = "Ans+"
                self.evalCharacter = f"{self.ans}+"
                return
            self.consoleCharacter = "+"
            self.evalCharacter = "+"
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def onButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def zeroButton(self, keyAttribute):
        if keyAttribute == 0:
            self.consoleCharacter = "0"
            self.evalCharacter = "0"
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def dotButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def negativeButton(self, keyAttribute):
        if keyAttribute == 0:
            self.notImplemented()
        if keyAttribute == 1:
            self.consoleCharacter = "Ans"
            self.evalCharacter = self.consoleLog[0]
            
        if keyAttribute == 2:
            self.notImplemented()
    def enterButton(self, keyAttribute):
        if keyAttribute == 0:
            if self.consoleText == "":
                # self.consoleLog.insert(0, self.consoleLog[1])
                # self.consoleLog.insert(0, self.consoleLog[1])
                # return
                self.consoleText = self.consoleLog[1]
                self.evalText = self.consoleLog[1]
            self.consoleLog.insert(0, self.consoleText)
            self.evalReply = self.runConsoleText()
            if self.evalReply != "None":
                self.ans = self.evalReply
            self.consoleLog.insert(0, str(self.evalReply))
            self.consoleCharacter = ""
            self.consoleText = ""
            self.evalCharacter = ""
            self.evalText = ""
            self.highlight_pos = [60, 192]
            print(self.consoleLog)
        if keyAttribute == 1:
            self.notImplemented()
        if keyAttribute == 2:
            self.notImplemented()
    def leftButton(self, keyAttribute):
        self.notImplemented()
    def rightButton(self, keyAttribute):
        self.notImplemented()
    def upButton(self, keyAttribute):
        self.notImplemented()
    def downButton(self, keyAttribute):
        self.notImplemented()
    def notImplemented(self):
        print("no")
        self.consoleCharacter = ""
        self.evalCharacter = ""
    def runConsoleText(self):
        if self.evalText != "":
            try:
                print(eval(self.evalText))
                return eval(self.evalText)
            except Exception as e:
                print(e)
                return "Error"
    def keyboardPresses(self, event):
        if event.type == pygame.KEYDOWN:
            mods = pygame.key.get_mods()
            if mods & pygame.KMOD_SHIFT:
                self.shiftPressed = 1
            else:
                self.shiftPressed = 0
            if mods & pygame.KMOD_CTRL:
                self.cntrlPressed = 1
            else:
                self.cntrlPressed = 0
            if mods & pygame.KMOD_ALT:
                self.altPressed = 1
            else:
                self.altPressed = 0
            self.keyPressed = event.key
            self.keyFull = (self.shiftPressed, self.cntrlPressed, self.altPressed, self.keyPressed)
            print(self.keyFull)
            self.update(self.keyFull)
            self.keyFull = (0, 0, 0, 0)
    def draw(self, surf, timey):
        self.time = timey
        surf.blit(self.screen, (52, 52))
        texty = text(self.text_pos, self.consoleText)
        self.highlight_pos[0] = 60 + texty[0]
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
        surf.blit(self.home_screen, (0, 0))
        if self.blink:
            if self.keyAttribute == 0:
                pygame.draw.rect(surf, (0, 0, 0), (self.highlight_pos[0], self.highlight_pos[1], 10, 15), 2)
            elif self.keyAttribute == 1:
                pygame.draw.polygon(surf, (0, 0, 0), [(self.highlight_pos[0], self.highlight_pos[1] + 5), (self.highlight_pos[0] + 5, self.highlight_pos[1]), (self.highlight_pos[0] + 10, self.highlight_pos[1] + 5), (self.highlight_pos[0] + 7, self.highlight_pos[1] + 4), (self.highlight_pos[0] + 7, self.highlight_pos[1] + 15), (self.highlight_pos[0] + 3, self.highlight_pos[1] + 15), (self.highlight_pos[0] + 3, self.highlight_pos[1] + 4)], 2)
            elif self.keyAttribute == 2:
                pygame.draw.polygon(surf, (0, 0, 0), [(self.highlight_pos[0], self.highlight_pos[1] + 15), (self.highlight_pos[0] + 3, self.highlight_pos[1] + 15), (self.highlight_pos[0] + 5, self.highlight_pos[1] + 10), (self.highlight_pos[0] + 7, self.highlight_pos[1] + 15), (self.highlight_pos[0] + 10, self.highlight_pos[1] + 15), (self.highlight_pos[0] + 5, self.highlight_pos[1])], 2)
                pygame.draw.polygon(surf, (0, 0, 0), [(self.highlight_pos[0] + 4, self.highlight_pos[1] + 10), (self.highlight_pos[0] + 6, self.highlight_pos[1] + 10), (self.highlight_pos[0] + 5, self.highlight_pos[1] + 8)], 2)
            if self.time > self.timeBlinked + .5:
                self.blink = not self.blink
                self.timeBlinked = time.time()
        else:
            if self.time > self.timeBlinked + .5:
                self.blink = not self.blink
                self.timeBlinked = time.time()