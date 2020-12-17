import pygame
from settings import *
from player import Player
from map import world_map

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
# установка количества кадров в секунду
clock = pygame.time.Clock()
# создание игрока
player = Player()

# основной цикл отрисовки
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # TODO: отраисовывать карту и игрока в ней
    clock.tick(FPS)
