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

# buttons = {
#     0: skip(),
#     1: "yEquals()",
#     2: "windowButton()",
#     3: "zoomButton()",
#     4: "traceButton()",
#     5: "graphButton()",
#     6: "secondButton()",
#     7: "modeButton()",
#     8: "delButton()",
#     9: "alphaButton()",
#     10: "xButton()",
#     11: "statButton()",
#     12: "mathButton()",
#     13: "appsButton()",
#     14: "prgmButton()",
#     15: "varsButton()",
#     16: "clearButton()",
#     17: "xToPowerMinusOneButton()",
#     18: "sinButton()",
#     19: "cosButton()",
#     20: "tanButton()",
#     21: "xToPowerOfButton()",
#     22: "xToPower2Button()",
#     23: "commaButton()",
#     24: "openParenthesisButton()",
#     25: "closeParenthesisButton()",
#     26: "divisionButton()",
#     27: "logButton()",
#     28: "sevenButton()",
#     29: "eightButton()",
#     30: "nineButton()",
#     31: "multiplicationButton()",
#     32: "lnButton()",
#     33: "fourButton()",
#     34: "fiveButton()",
#     35: "sixButton()",
#     36: "minusButton()",
#     37: "stoButton()",
#     38: "oneButton()",
#     39: "twoButton()",
#     40: "threeButton()",
#     41: "plusButton()",
#     42: "onButton()",
#     43: "zeroButton()",
#     44: "dotButton()",
#     45: "negativeButton()",
#     46: "enterButton()",
#     47: "leftButton()",
#     48: "rightButton()",
#     49: "upButton()",
#     50: "downButton()"
# }
