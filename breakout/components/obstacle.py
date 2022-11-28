import pygame
import random


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image, speed, shell=False):
        super().__init__()
        self.original_image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (50, 50))
        self.rect = self.image.get_rect()
        self.shell = shell
        if self.shell == False:
            self.rect.y = random.randint(10, 300)
        else:
            self.rect.y = 360
        self.rect.x = 805
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed
