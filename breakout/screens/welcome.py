import pygame
from screens import BaseScreen
from components import TextBox
from ..components import Background


class WelcomeScreen(BaseScreen):
    '''Creating welcome screen'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.score = None
        self.background = Background('./images/background5.jpg')
        self.sprites = pygame.sprite.Group()
        self.button = TextBox(
            (300, 100), "Press SPACE to start", color=(0, 0, 0), bgcolor=(255, 255, 255)
        )
        self.sprites.add(self.button)

    def draw(self):
        '''draw the screen'''
        self.window.fill((255, 255, 255))
        self.window.blit(self.background.image_scaled, self.background.rect)
        self.button.rect.x = 170
        self.button.rect.y = 160
        self.sprites.draw(self.window)

    def update(self):
        pass

    def manage_event(self, event):
        '''adding event'''
        print(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_screen = "game"
            self.running = False
