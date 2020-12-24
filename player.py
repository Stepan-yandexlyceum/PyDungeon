from settings import *
from Character import *
import pygame


class Player(Character):
    image = pygame.image.load("data/Knight_01_right.png")

    def __init__(self, weapon, armor, screen, sprites):
        super().__init__(weapon, armor, sprites)
        self.x, self.y = player_pos
        self.rect = self.image.get_rect()


    def movement(self):
        keys = pygame.key.get_pressed()

        # управление игроком производится клавишами w,a,s,d
        if keys[pygame.K_w]:
            self.rect.y += 10
        if keys[pygame.K_a]:
            self.rect.x -= 10
            self.image = pygame.image.load("data/Knight_01_left.png")
        if keys[pygame.K_s]:
            self.rect.y -= 10
        if keys[pygame.K_d]:
            self.rect.x += 10
            self.image = pygame.image.load("data/Knight_01_right.png")

        if keys[pygame.K_DOWN]:
            self.rect.y += 10
        if keys[pygame.K_LEFT]:
            self.rect.x -= 10
            self.image = pygame.image.load("data/Knight_01_left.png")
        if keys[pygame.K_UP]:
            self.rect.y -= 10
        if keys[pygame.K_RIGHT]:
            self.rect.x += 10
            self.image = pygame.image.load("data/Knight_01_right.png")

