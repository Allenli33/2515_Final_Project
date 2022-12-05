import pygame


class Background(pygame.sprite.Sprite):
    '''adding background sprite class'''

    def __init__(self, image_file, location=[0, 0]):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.image_scaled = pygame.transform.scale(self.image, (800, 400))
        self.rect = self.image_scaled.get_rect()
        self.rect.left, self.rect.top = location
