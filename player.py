from Items import *
from map import text_map
from settings import *
from Character import *
import pygame


class Player(Character):
    image = pygame.image.load("data/image/knight.png")
    image = pygame.transform.scale(image, (cell_size, cell_size))

    def __init__(self, screen, sprites, weapon=None, armor=None, helmet=None, leg=None):
        super().__init__(weapon, armor, helmet, leg, sprites)
        self.x, self.y = player_pos
        self.rect = pygame.Rect(self.x * cell_size, self.y * cell_size, cell_size, cell_size)
        self.direction = 'right'
        self.health = 20
        self.max_health = 20
        self.weapon = weapon
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
                sc = pygame.display.set_mode((WIDTH + 300, HEIGHT))

            self.is_inventory_print = not self.is_inventory_print

    def get_armor(self):
        if self.armor is Armor:
            return self.armor

    def get_helmet(self):
        if self.helmet is Armor:
            return self.helmet

    def get_leg(self):
        if self.leg is Armor:
            return self.leg
