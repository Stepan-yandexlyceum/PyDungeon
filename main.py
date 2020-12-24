import pygame
import os
import sys
from settings import *
from player import Player
from map import *
from Character import Character
from Armor import Armor
from Weapon import Weapon
from Enemy import Enemy

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
# установка количества кадров в секунду
clock = pygame.time.Clock()



def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

texture_wall = load_image("image/textures_dungeon_001.png")
# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()

# создадим начальное снаряжение для игрока (потом переденесем в БД, но потом)
wooden_baton = Weapon("деревянная дубина", 3, 2)
leather_cuirass = Armor("кожаная кираса", 0, 1)

# создадим игрока
hero = Player(wooden_baton, leather_cuirass, sc, all_sprites)

running = True
# основной цикл отрисовки
while True:
    for event in pygame.event.get():
        sc.fill((0, 0, 0))

        if event.type == pygame.QUIT:
            running = False

        # движение игрока
        hero.movement()
    for i in range(map_height):
        for j in range(map_width):
            if text_map[i][j] == 'w':
                sc.blit(texture_wall, (32 * i, 32 * j))
    all_sprites.draw(sc)
    pygame.display.flip()
    # TODO: отраисовывать карту и игрока в ней
    clock.tick(FPS)
