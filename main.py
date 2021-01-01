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
from level_generation import draw_map

pygame.init()

# установка количества кадров в секунду
clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["ДОБРО ПОЖАЛОВАТЬ В PYDUNGEON",
                  "Для того, чтобы выбраться от сюда,",
                  "Вам понадобится пройти три уровня катакомб и побороть невиданных чудищ",
                  "Если Вы псих, нажмите любую кнопку"]

    fon = pygame.transform.scale(load_image('image/dungeon_intro.jpeg'), (WIDTH, HEIGHT))
    sc.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('yellow'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        sc.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()


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
            print("WIN")
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
