from settings import *
from Character import *
import pygame


class Player(Character):
    image = pygame.image.load("data/Knight_01_right.png")
    image = pygame.transform.scale(image, (32, 32))

    def __init__(self, weapon, armor, screen, sprites):
        super().__init__(weapon, armor, sprites)
        self.x, self.y = player_pos
        self.rect = self.image.get_rect()
        self.direction = 'right'

    def movement(self):
        keys = pygame.key.get_pressed()

        # управление игроком производится клавишами w,a,s,d
        if keys[pygame.K_w]:
            self.rect.y += -32
        if keys[pygame.K_a]:
            self.rect.x -= 32
            self.flip_image('left')
        if keys[pygame.K_s]:
            self.rect.y -= -32
        if keys[pygame.K_d]:
            self.rect.x += 32
            self.flip_image('right')

        if keys[pygame.K_DOWN]:
            self.rect.y += 32
        if keys[pygame.K_LEFT]:
            self.rect.x -= 32
            self.flip_image('left')
        if keys[pygame.K_UP]:
            self.rect.y -= 32
        if keys[pygame.K_RIGHT]:
            self.rect.x += 32
            self.flip_image('right')

    def flip_image(self, direction):
        if direction != self.direction:
            self.image = pygame.transform.flip(self.image, True, False)
            if self.direction == 'right':
                self.direction = 'left'
            else:
                self.direction = 'right'