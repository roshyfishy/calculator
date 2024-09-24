import pygame

pygame.init()
nativeres = pygame.display.Info()
resw = nativeres.current_w
resh = nativeres.current_h
resw = 320
resh = 720
sfx = resw/320
sfy = resh/720
resmulti = resw / 2560
fontmulti = resh / 1440
screen = pygame.display.set_mode((resw, resh))
hell = pygame.Rect(39, 306, 43, 24)
rectangles = [
    (pygame.Rect(42, 248, 41, 17), 1),  # yEqualsButton
    (pygame.Rect(90, 251, 40, 16), 2),  # windowButton
    (pygame.Rect(138, 252, 41, 16), 3),  # zoomButton
    (pygame.Rect(187, 251, 40, 16), 4),  # traceButton
    (pygame.Rect(234, 248, 42, 17), 5),  # graphButton
    (pygame.Rect(39, 306, 43, 24), 6),  # secondButton
    (pygame.Rect(90, 312, 40, 23), 7),  # modeButton
    (pygame.Rect(138, 314, 40, 23), 8),  # delButton
    (pygame.Rect(39, 341, 43, 24), 9),  # alphaButton
    (pygame.Rect(90, 347, 40, 23), 10),  # xButton
    (pygame.Rect(138, 349, 40, 23), 11),  # statButton
    (pygame.Rect(39, 376, 43, 24), 12),  # mathButton
    (pygame.Rect(90, 381, 40, 23), 13),  # appsButton
    (pygame.Rect(138, 383, 40, 23), 14),  # prgmButton
    (pygame.Rect(185, 382, 41, 23), 15),  # varsButton
    (pygame.Rect(233, 375, 42, 25), 16),  # clearButton
    (pygame.Rect(39, 412, 43, 24), 17),  # xToPowerMinusOneButton
    (pygame.Rect(90, 417, 40, 23), 18),  # sinButton
    (pygame.Rect(138, 419, 40, 23), 19),  # cosButton
    (pygame.Rect(185, 418, 41, 23), 20),  # tanButton
    (pygame.Rect(233, 411, 42, 25), 21),  # xToPowerOfButton
    (pygame.Rect(39, 449, 43, 24), 22),  # xToPower2Button
    (pygame.Rect(90, 454, 40, 23), 23),  # commaButton
    (pygame.Rect(138, 456, 40, 23), 24),  # openParenthesisButton
    (pygame.Rect(185, 455, 41, 23), 25),  # closeParenthesisButton
    (pygame.Rect(233, 448, 42, 25), 26),  # divisionButton
    (pygame.Rect(39, 485, 43, 24), 27),  # logButton
    (pygame.Rect(90, 491, 40, 30), 28),  # sevenButton
    (pygame.Rect(138, 494, 40, 30), 29),  # eightButton
    (pygame.Rect(185, 491, 41, 30), 30),  # nineButton
    (pygame.Rect(233, 484, 42, 25), 31),  # multiplicationButton
    (pygame.Rect(39, 522, 43, 24), 32),  # lnButton
    (pygame.Rect(90, 541, 40, 30), 33),  # fourButton
    (pygame.Rect(138, 544, 40, 30), 34),  # fiveButton
    (pygame.Rect(185, 541, 41, 30), 35),  # sixButton
    (pygame.Rect(233, 521, 42, 25), 36),  # minusButton
    (pygame.Rect(39, 562, 43, 24), 37),  # stoButton
    (pygame.Rect(90, 588, 40, 30), 38),  # oneButton
    (pygame.Rect(138, 591, 40, 30), 39),  # twoButton
    (pygame.Rect(185, 588, 41, 30), 40),  # threeButton
    (pygame.Rect(233, 561, 42, 25), 41),  # plusButton
    (pygame.Rect(45, 603, 43, 29), 42),  # onButton
    (pygame.Rect(90, 638, 40, 30), 43),  # zeroButton
    (pygame.Rect(138, 641, 40, 30), 44),  # dotButton
    (pygame.Rect(185, 638, 41, 30), 45),  # negativeButton
    (pygame.Rect(233, 598, 42, 41), 46),  # enterButton
    (pygame.Rect(191, 313, 24, 33), 47),  # leftButton
    (pygame.Rect(259, 311, 26, 35), 48),  # rightButton
    (pygame.Rect(220, 288, 35, 42), 49),  # upButton
    (pygame.Rect(220, 331, 35, 40), 50),  # downButton
]
def checkcollisions(mouse_pos):
    for rect, value in rectangles:
        if rect.collidepoint(mouse_pos):
            return value
    return 0
def displayHitboxes(surf):
    for rect, value in rectangles:
        pygame.draw.rect(surf, (255, 0, 0), rect)
font1 = pygame.font.SysFont("fonts\\PixelOperator-Bold.ttf", 25)
def text(coords, text, Offset = False, display = screen, font = font1, text_alpha = 255, text_color = (0, 0, 0)):
    texty = font.render(text, True, text_color)
    texty.set_alpha(text_alpha)
    x, y = coords
    if Offset:
        x -= texty.get_width()
    display.blit(texty, (x, y))
    return texty.get_width(), texty.get_height()
# def startPlotButton(self, keyAttribute):
#     self.notImplemented()
# def tableSetupButton(self, keyAttribute):
#     self.notImplemented()
# def formatButton(self, keyAttribute):
#     self.notImplemented()
# def calcButton(self, keyAttribute):
#     self.notImplemented()
# def tableButton(self, keyAttribute):
#     self.notImplemented()
# def quitButton(self, keyAttribute):
#     self.notImplemented()
# def insertButton(self, keyAttribute):
#     self.notImplemented()
# def aLockButton(self, keyAttribute):
#     self.notImplemented()
# def linkButton(self, keyAttribute):
#     self.notImplemented()
# def listButton(self, keyAttribute):
#     self.notImplemented()
# def testButton(self, keyAttribute):
#     self.notImplemented()
# def angleButton(self):
#     self.notImplemented()
# def drawButton(self):
#     self.notImplemented()
# def distrButton(self):
#     self.notImplemented()
# def matrixButton(self):
#     self.notImplemented()
# def sinMinus1Button(self):
#     self.notImplemented()
# def cosMinus1Button(self):
#     self.notImplemented()
# def tanMinus1Button(self):
#     self.notImplemented()
# def pieButton(self):
#     self.notImplemented()
# def sqrtButton(self):
#     self.notImplemented()
# def eeButton(self):
#     self.notImplemented()
# def openCurlyBracketButton(self):
#     self.notImplemented()
# def closeCurlyBracketButton(self):
#     self.notImplemented()
# def eButton(self):
#     self.notImplemented()
# def tenToXButton(self):
#     self.notImplemented()
# def uButton(self):
#     self.notImplemented()
# def vButton(self):
#     self.notImplemented()
# def wButton(self):
#     self.notImplemented()
# def openBracketButton(self):
#     self.notImplemented()
# def eToXButton(self):
#     self.notImplemented()
# def l4Button(self):
#     self.notImplemented()
# def l5Button(self):
#     self.notImplemented()
# def l6Button(self):
#     self.notImplemented()
# def closeBracketButton(self):
#     self.notImplemented()
# def rclButton(self):
#     self.notImplemented()
# def l1Button(self):
#     self.notImplemented()
# def l2Button(self):
#     self.notImplemented()
# def l3Button(self):
#     self.notImplemented()
# def memButton(self):
#     self.notImplemented()
# def offButton(self):
#     self.notImplemented()
# def catalogButton(self):
#     self.notImplemented()
# def iButton(self):
#     self.notImplemented()
# def ansButton(self):
#     self.notImplemented()
# def entryButton(self):
#     self.notImplemented()
# def f1Button(self):
#     self.notImplemented()
# def f2Button(self):
#     self.notImplemented()
# def f3Button(self):
#     self.notImplemented()
# def f4Button(self):
#     self.notImplemented()
# def f5Button(self):
#     self.notImplemented()
# def letterAButton(self):
#     self.notImplemented()
# def letterBButton(self):
#     self.notImplemented()
# def letterCButton(self):
#     self.notImplemented()
# def letterDButton(self):
#     self.notImplemented()
# def letterEButton(self):
#     self.notImplemented()
# def letterFButton(self):
#     self.notImplemented()
# def letterGButton(self):
#     self.notImplemented()
# def letterHButton(self):
#     self.notImplemented()
# def letterIButton(self):
#     self.notImplemented()
# def letterJButton(self):
#     self.notImplemented()
# def letterKButton(self):
#     self.notImplemented()
# def letterLButton(self):
#     self.notImplemented()
# def letterMButton(self):
#     self.notImplemented()
# def letterNButton(self):
#     self.notImplemented()
# def letterOButton(self):
#     self.notImplemented()
# def letterPButton(self):
#     self.notImplemented()
# def letterQButton(self):
#     self.notImplemented()
# def letterRButton(self):
#     self.notImplemented()
# def letterSButton(self):
#     self.notImplemented()
# def letterTButton(self):
#     self.notImplemented()
# def letterUButton(self):
#     self.notImplemented()
# def letterVButton(self):
#     self.notImplemented()
# def letterWButton(self):
#     self.notImplemented()
# def letterXButton(self):
#     self.notImplemented()
# def letterYButton(self):
#     self.notImplemented()
# def letterZButton(self):
#     self.notImplemented()
# def emptySetButton(self):
#     self.notImplemented()
# def quotationMarksButton(self):
#     self.notImplemented()
# def spaceButton(self):
#     self.notImplemented()
# def colonButton(self):
#     self.notImplemented()
# def questionMarkButton(self):
#     self.notImplemented()
# def solveButton(self):
#     self.notImplemented()    