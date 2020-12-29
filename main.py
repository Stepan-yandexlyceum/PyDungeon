import pygame
import os
import sys
from settings import *
from Chest import *
from player import Player
from map import *
from Character import Character
from Armor import Armor
from Items import Item, Enemy, Potion, Weapon
from functions import *

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
# установка количества кадров в секунду
clock = pygame.time.Clock()
# количество предметов на каждом уровне - монстры, оружие, зелья
level1 = [5, 6, 8]
level2 = [7, 3, 5]
level3 = [10, 1, 3]


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


texture_wall = load_image("image/textures_dungeon_001.png")
texture_floor = load_image("image/dark-brick-wall-texture_1048-7626.jpg")
texture_floor = pygame.transform.scale(texture_floor, (cell_size, cell_size))
# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()
character_sprites = pygame.sprite.Group()

# создадим игрока
hero = Player(sc, character_sprites)

running = True
# основной цикл отрисовки
start = False
start_screen()

# добавляем объекты на карте
enemies = []
for i in range(level1[0]):
    # TODO: fix this
    monster = Enemy('enemy', random.choice(["Ghost", "Minotaur", "Golem"]), character_sprites)
    enemies.append(monster)

while True:
    sc.fill((0, 0, 0))
    for event in pygame.event.get():
        sc.fill((0, 0, 0))
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            hero.movement()
        if hero.x >= map_width - 1:
            # TODO: сообщение о победе и переход на новый уровень
            print("WIN")
            break

        # рисуем карту
        for i in range(map_height):
            for j in range(map_width):
                if text_map[i][j] == 'w':
                    sc.blit(texture_wall, (cell_size * i, cell_size * j))
                if text_map[i][j] == 'c':
                    sc.blit(texture_floor, (cell_size * i, cell_size * j))

        for enemy in enemies:
            for i in range(map_height):
                for j in range(map_width):
                    if (i, j) == enemy.get_pos():
                        sc.blit(enemy.image, (cell_size * i, cell_size * j))
        # рисуем полостку здоровья
        pygame.draw.rect(sc, pygame.Color('red'), (0, HEIGHT - 10, hero.health * 10, HEIGHT))
        all_sprites.draw(sc)
        character_sprites.draw(sc)
        pygame.display.flip()
    clock.tick(FPS)
