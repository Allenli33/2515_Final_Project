import pygame
from screens import BaseScreen
from components import TextBox
from ..components import Background


class WelcomeScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.background = Background('./images/background4.png')
        self.sprites = pygame.sprite.Group()
        self.button = TextBox(
            (400, 100), "Press SPACE to start", color=(255, 255, 255), bgcolor=(0, 0, 0)
        )
        self.sprites.add(self.button)

    def draw(self):
        self.window.fill((255, 255, 255))
        self.window.blit(self.background.image_scaled, self.background.rect)
        self.button.rect.x = 200
        self.button.rect.y = 150
        self.sprites.draw(self.window)

    def update(self):
        pass

    def manage_event(self, event):
        print(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_screen = "game"
            self.running = False
