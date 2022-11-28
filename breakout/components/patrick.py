import pygame
pygame.mixer.init()


class Patrick(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        patrick_walk_1 = pygame.image.load(
            './images/patrick/patrick_1.png').convert_alpha()
        patrick_walk_2 = pygame.image.load(
            './images/patrick/patrick_2.png').convert_alpha()
        patrick_walk_3 = pygame.image.load(
            './images/patrick/patrick_3.png').convert_alpha()

        self.patrick_walk = [patrick_walk_1, patrick_walk_2, patrick_walk_3]
        self.patrick_index = 0
        self.patrick_jump = pygame.image.load(
            './images/patrick/patrick_4.png').convert_alpha()

        self.image = self.patrick_walk[self.patrick_index]
        self.rect = self.image.get_rect(midbottom=(50, 360))
        self.gravity = 0

        # self.jump_sound = pygame.mixer.Sound('./sound/jump.mp3')
        # self.jump_sound.set_volume(0.5)

    def patrick_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.gravity = -5
            # self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 0.5
        self.rect.y += self.gravity

    def animation_state(self):
        if self.rect.bottom < 360:
            self.image = self.patrick_jump
        if self.rect.bottom >= 400:
            self.rect.bottom = 400
        if self.rect.top <= -50:
            self.rect.top = -50
        else:
            self.patrick_index += 0.1
            if self.patrick_index >= len(self.patrick_walk):
                self.patrick_index = 0
            self.image = self.patrick_walk[int(self.patrick_index)]

    def update(self):
        self.patrick_input()
        self.apply_gravity()
        self.animation_state()
