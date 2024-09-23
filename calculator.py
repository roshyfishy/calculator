try: 
    import os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
    import subprocess
    import pygame
    import sys
    import traceback
    from time import time
    from pygame.locals import KEYDOWN
    from calculatorstuffs.buttons import *
    from calculatorstuffs.Console import Console
    import math as meth
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "-r", "calculatorstuffs\\requirements.txt"])
    import os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
    import subprocess
    import pygame
    import sys
    import traceback
    from time import time
    from pygame.locals import KEYDOWN
    from calculatorstuffs.buttons import *
    from calculatorstuffs.Console import Console
    import math as meth

pygame.init()
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

screen1 = pygame.Surface((resw, resh))
screen1.set_alpha(0)
pygame.display.set_caption('calculator')
# icon = pygame.image.load("assets/pizza.png")
# pygame.display.set_icon(icon)
last_time = time()
home_screen = pygame.image.load('calculatorstuffs/assets/ti-84boxes.png')
home_screen = pygame.transform.smoothscale(home_screen, (320, 720))



class Game():
    def __init__(self):
        super().__init__()
        self.level_done = False
        self.mouse_pos = (-1, -1)
        self.showHitboxes = False
        self.console_instance = Console()
    def start(self):
        pass
    def get_event(self, event):
        if event.type == KEYDOWN:
            if  event.key == pygame.K_ESCAPE or event.key == pygame.K_z:
                self.level_done = True
            if event.key == pygame.K_q:
                    x, y = pygame.mouse.get_pos()
                    print(f"Mouse Position: X={x}, Y={y}")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.mouse_pos = pygame.mouse.get_pos()
        self.console_instance.keyboardPresses(event)
    def update(self, surf=screen):
        if self.mouse_pos != (-1, -1):
            self.buttonPressed = checkcollisions(self.mouse_pos)
            self.console_instance.update(self.buttonPressed)
            self.mouse_pos = (-1, -1)
    def draw(self, surf=screen):
        self.console_instance.draw(surf)
        if self.showHitboxes == True:
            displayHitboxes(surf)


class GameRunner():
    def __init__(self, screen, states, start_state) -> None:
        self.screen = screen
        self.states = states
        self.start_state = start_state
        self.state = self.states[self.start_state]

        self.state.start()
        self.run()
    def run(self):
            running = True
            while running:
                self.get_events()
                self.update()
                self.draw()       
    def get_events(self):
        if self.state.level_done == True:
            self.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            self.state.get_event(event)
    def update(self):
        self.state.update()
    def draw(self):
        # pygame.display.set_icon(pygame.image.load('assets/player_idle1.png'))
        pygame.display.set_caption(f'calculator - Pygame. FPS: {int(clock.get_fps())}')
        clock.tick(60)
        pygame.display.update()
        self.state.draw(self.screen)
    def quit(self):
        pygame.quit()
        sys.exit()
if __name__ == "__main__":
    states = {
        "Menu":     "Menu()",
        "Game":     Game(),
        "Pause":    "Pause()",
        "Exit":     "Exit()",
        "Options":  "Options()",
        "GameOver": "GameOver()"
    }
    try:
        GameRunner(screen, states, "Game")
    except Exception as e:
        traceback.print_exc()
        pygame.quit()
        sys.exit()