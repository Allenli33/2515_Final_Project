import random
import pygame
from screens import BaseScreen

from ..components import Patrick, Background, Obstacle
from components import TextBox


class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.patrick = Patrick()
        self.background = Background('./images/background4.png')
        self.obstacle_group = pygame.sprite.Group()
        self.patty = pygame.sprite.Group()
        self.score = 1
        self.lives = 5
        self.font = pygame.font.SysFont('Consolas', 30)

    def update(self):
        self.patrick.update()
        self.patrick_animation()
        self.obstacle_group.update()
        self.patty.update()
        self.manage_enemies()
        self.text_score = self.font.render(
            f'Score:{str(self.score)}', True, (0, 0, 0))
        self.lives_score = self.font.render(
            f'HP:{self.lives}', True, (0, 0, 0))

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT]:
        #     self.paddle.move("left")

        # if keys[pygame.K_RIGHT]:
        #     self.paddle.move("right")

        # self.sprites.update()
        # collided = self.ball.collidetiles(self.tiles)

        # caught_the_ball = self.ball.collidepaddle(self.paddle.rect)

        # if self.ball.rect.bottom > self.paddle.rect.top and not caught_the_ball:
        #     self.running = False
        #     self.next_screen = "game_over"
        pass

    def draw(self):
        self.window.fill((255, 255, 255))
        self.window.blit(self.background.image_scaled, self.background.rect)
        self.window.blit(self.patrick_surf, self.patrick.rect)
        self.obstacle_group.draw(self.window)
        self.patty.draw(self.window)
        self.window.blit(self.text_score, (600, 20))
        self.window.blit(self.lives_score, (100, 20))

    def manage_event(self, event):
        pass

    def patrick_animation(self):
        if self.patrick.rect.bottom < 360:
            # jump
            self.patrick_surf = self.patrick.patrick_jump
        else:
            # walk
            self.patrick.patrick_index += 0.1
            if self.patrick.patrick_index >= len(self.patrick.patrick_walk):
                self.patrick.patrick_index = 0
            self.patrick_surf = self.patrick.patrick_walk[int(
                self.patrick.patrick_index)]

    def manage_enemies(self):
        if random.randrange(0, 100) < 1:
            if random.randint(0, 1) == 0:
                enemy = Obstacle("./images/plankton/Plankton3.png", 6)
                self.obstacle_group.add(enemy)
            else:
                enemy = Obstacle("./images/shell.png", 6, True)
                self.obstacle_group.add(enemy)
        if random.randrange(0, 100) < 1:
            good = Obstacle("./images/patty.png", 10)
            self.patty.add(good)
        if pygame.sprite.spritecollide(self.patrick, self.obstacle_group, dokill=True):
            self.lives -= 1
            if self.lives <= 0:
                self.next_screen = "game_over"
                self.running = False
        if pygame.sprite.spritecollide(self.patrick, self.patty, dokill=True):
            self.score += 1

            if self.score % 20 == 0:
                self.lives += 1
