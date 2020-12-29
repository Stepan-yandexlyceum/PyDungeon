from map import text_map
from settings import *
from Character import *
import pygame


class Player(Character):
    image = pygame.image.load("data/image/Knight_01_right.png")
    image = pygame.transform.scale(image, (cell_size, cell_size))

    def __init__(self, screen, sprites, weapon="", armor=""):
        super().__init__(weapon, armor, sprites)
        self.x, self.y = player_pos
        self.rect = pygame.Rect(self.x * cell_size, self.y * cell_size, cell_size, cell_size)
        self.direction = 'right'
        self.health = 20

        self.inventory = [None for i in range(15)]
        self.is_inventory_print = False

    def pos(self):
        return self.x, self.y

    def get_health(self):
        return self.health

    def movement(self):
        keys = pygame.key.get_pressed()

        y = self.rect.y
        x = self.rect.x
        m_y = self.y
        m_x = self.x
        # управление игроком производится клавишами w,a,s,d
        if keys[pygame.K_w]:
            self.rect.y += -cell_size
            self.y -= 1
        if keys[pygame.K_a]:
            self.rect.x -= cell_size
            self.x -= 1
            self.flip_image('left')
        if keys[pygame.K_s]:
            self.rect.y += cell_size
            self.y += 1
        if keys[pygame.K_d]:
            self.rect.x += cell_size
            self.x += 1
            self.flip_image('right')

        if keys[pygame.K_DOWN]:
            self.rect.y += cell_size
            self.y += 1
        if keys[pygame.K_LEFT]:
            self.rect.x -= cell_size
            self.x -= 1
            self.flip_image('left')
        if keys[pygame.K_UP]:
            self.rect.y -= cell_size
            self.y -= 1
        if keys[pygame.K_RIGHT]:
            self.rect.x += cell_size
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

    def get_is_inventory_print(self):
        return self.is_inventory_prints

    def print_inventory(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_e]:
            if self.is_inventory_print:
                sc = pygame.display.set_mode((WIDTH, HEIGHT))
            else:
                sc = pygame.display.set_mode((WIDTH_MAP_AND_INVENTORY, HEIGHT))

            self.is_inventory_print = not self.is_inventory_print

