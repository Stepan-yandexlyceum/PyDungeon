from map import text_map
from settings import *
from Character import *
import pygame


class Player(Character):
    image = pygame.image.load("data/Knight_01_right.png")
    image = pygame.transform.scale(image, (32, 32))

    def __init__(self, weapon, armor, screen, sprites):
        super().__init__(weapon, armor, sprites)
        self.x, self.y = player_pos
        self.rect = pygame.Rect(self.x * 32, self.y * 32, 32, 32)
        self.direction = 'right'

    def pos(self):
        return self.x, self.y

    def movement(self):
        keys = pygame.key.get_pressed()

        y = self.rect.y
        x = self.rect.x
        m_y = self.y
        m_x = self.x
        # управление игроком производится клавишами w,a,s,d
        if keys[pygame.K_w]:
            self.rect.y += -32
            self.y -= 1
        if keys[pygame.K_a]:
            self.rect.x -= 32
            self.x -= 1
            self.flip_image('left')
        if keys[pygame.K_s]:
            self.rect.y += 32
            self.y += 1
        if keys[pygame.K_d]:
            self.rect.x += 32
            self.x += 1
            self.flip_image('right')

        if keys[pygame.K_DOWN]:
            self.rect.y += 32
            self.y += 1
        if keys[pygame.K_LEFT]:
            self.rect.x -= 32
            self.x -= 1
            self.flip_image('left')
        if keys[pygame.K_UP]:
            self.rect.y -= 32
            self.y -= 1
        if keys[pygame.K_RIGHT]:
            self.rect.x += 32
            self.x += 1
            self.flip_image('right')

        if text_map[self.x][self.y] == 'w':
            self.rect.y = y
            self.rect.x = x
            self.y = m_y
            self.x = m_x
            

    def flip_image(self, direction):
        if direction != self.direction:
            self.image = pygame.transform.flip(self.image, True, False)
            if self.direction == 'right':
                self.direction = 'left'
            else:
                self.direction = 'right'