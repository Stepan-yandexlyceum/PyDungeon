from settings import *
from Character import *
import pygame


class Player(Character):
    def __init__(self):
        self.x, self.y = player_pos

    @property
    def pos(self):
        return self.x, self.y

    def movement(self):
        keys = pygame.key.get_pressed()

        # управление игроком производится клавишами w,a,s,d
        if keys[pygame.K_w]:
            self.y += 1
        if keys[pygame.K_a]:
            self.x += -1
        if keys[pygame.K_s]:
            self.y += -1
        if keys[pygame.K_d]:
            self.x += 1

        if keys[pygame.K_DOWN]:
            self.y += 1
        if keys[pygame.K_LEFT]:
            self.x += -1
        if keys[pygame.K_UP]:
            self.y += -1
        if keys[pygame.K_RIGHT]:
            self.x += 1
