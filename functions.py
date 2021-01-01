import os
import sys
import pygame
from settings import *

sc = pygame.display.set_mode((WIDTH, HEIGHT))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


texture_wall = load_image("image/Brick_Wall_009.jpg")
texture_wall = pygame.transform.scale(texture_wall, (cell_size * 2, cell_size * 2))
texture_floor = load_image("image/dark-brick-wall-texture_1048-7626.jpg")
texture_floor = pygame.transform.scale(texture_floor, (cell_size, cell_size))
# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()
character_sprites = pygame.sprite.Group()
