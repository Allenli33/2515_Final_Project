import pygame
import requests
import uuid
from screens import BaseScreen
from components import TextBox
from ..components import Background


class GameOverScreen(BaseScreen):
    '''Creating game over screen'''

    def __init__(self, window, score):
        super().__init__(self)
        self.window = window
        self.score = score
        self.background = Background('./images/gameover.jpeg')
        self.sprites = pygame.sprite.Group()
        self.button1 = TextBox(
            (200, 100), "Restart", color=(255, 0, 0), bgcolor=(120, 120, 120)
        )
        self.button2 = TextBox(
            (200, 100), "Quit", color=(0, 255, 0), bgcolor=(255, 140, 70)
        )
        self.button1.rect.topleft = (75, 150)
        self.button2.rect.topleft = (500, 150)
        self.sprites.add(self.button1, self.button2)
        self.text = pygame.font.SysFont("calibri", size=40)
        self.record = False

    def draw(self):
        '''draw the screen'''
        self.window.fill((255, 255, 255))
        self.window.blit(self.background.image_scaled, self.background.rect)
        self.sprites.draw(self.window)
        self.text_surf = self.text.render(
            f"Final Score: {self.score} ", (200, 200), (255, 255, 255))
        self.window.blit(self.text_surf, (280, 0))

    def manage_event(self, event):
        '''adding event'''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button1.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "welcome"
            elif self.button2.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = False

    def update(self):
        '''check record'''
        if self.record == False:
            self.record = True
            score = {
                "score": self.score,
                "id": str(uuid.uuid4())
            }
            requests.post("http://127.0.0.1:5000/add/score", json=score)
