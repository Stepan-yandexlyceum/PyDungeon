from settings import *
import pygame


class Player:
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
