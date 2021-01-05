import pygame
import os
import sys
from settings import *
from player import Player
from map import *
from Character import Character
from Items import *
from functions import *
from random import choices
from music_player import play_music
from level_generation import draw_map, cur_level

pygame.init()

# установка количества кадров в секунду
clock = pygame.time.Clock()

# создадим игрока
hero = Player(sc, character_sprites)

running = True
# основной цикл отрисовки
start = False
play_music("data\music\main_theme.mp3")
start_screen()

while True:
    sc.fill((0, 0, 0))
    for event in pygame.event.get():
        sc.fill((0, 0, 0))
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            hero.movement()
            hero.print_inventory()
        if hero.x >= map_width - 1:
            # TODO: сообщение о победе и переход на новый уровень
            level2_screen()
            cur_level += 1
            break
        draw_map()
        # рисуем полостку здоровья
        pygame.draw.rect(sc, pygame.Color('red'), (0, HEIGHT - 10, hero.health * 10, HEIGHT))
        if hero.get_is_inventory_print:
            pygame.draw.line(sc, (255, 0, 0), (1200, 0), (1200, 800), 2)
        all_sprites.draw(sc)
        character_sprites.draw(sc)
        pygame.display.flip()
    clock.tick(FPS)
