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

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
# установка количества кадров в секунду
clock = pygame.time.Clock()
# количество предметов на каждом уровне - монстры, оружие,броня, зелья
level1 = [5, 6, 5, 8]
level2 = [7, 3, 4, 5]
level3 = [10, 1, 2, 3]


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


texture_wall = load_image("image/Brick_Wall_009.jpg")
texture_wall = pygame.transform.scale(texture_wall, (cell_size * 2, cell_size * 2))
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
play_music("data\music\main_theme.mp3")
start_screen()

# добавляем объекты на карте
# добавляем врагов
enemies = []
for i in range(level1[0]):
    monster = Enemy('enemy', random.choice(["Ghost", "Minotaur", "Golem"]), character_sprites)
    enemies.append(monster)
# добавляем оружие
weapons = []
for i in range(level1[1]):
    weapon = Weapon('weapon', random.choice(["Double_Axe", "Hammer", "Stick", "Sword"]), character_sprites)
    weapons.append(weapon)
armor = []
for i in range(level1[2]):
    arm = Armor('armor', random.choice(["Helmet1", "Helmet2", "Cuiras1", "Cuiras2", "Arm_armor1", "Arm_armor2",
                                        "Leg_armor1", "Leg_armor2"]), character_sprites)
    armor.append(arm)
potions = []
for i in range(level1[3]):
    potion = Potion('potion', random.choice(["Small_health", "Small_strength"]), character_sprites)
    potions.append(potion)
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

        # рисуем карту
        for i in range(map_height):
            for j in range(map_width):
                if text_map[i][j] == 'w':
                    sc.blit(texture_wall, (cell_size * i, cell_size * j))
                if text_map[i][j] == 'c':
                    sc.blit(texture_floor, (cell_size * i, cell_size * j))
        # рисуем монстров
        for enemy in enemies:
            for i in range(map_height):
                for j in range(map_width):
                    if (i, j) == enemy.get_pos():
                        sc.blit(enemy.image, (cell_size * i, cell_size * j))
        # рисуем оружие
        for weapon in weapons:
            for i in range(map_height):
                for j in range(map_width):
                    if (i, j) == weapon.get_pos():
                        sc.blit(weapon.image, (cell_size * i, cell_size * j))
        # рисуем броню
        for arm in armor:
            for i in range(map_height):
                for j in range(map_width):
                    if (i, j) == arm.get_pos():
                        sc.blit(arm.image, (cell_size * i, cell_size * j))
        # рисуем зелья
        for potion in potions:
            for i in range(map_height):
                for j in range(map_width):
                    if (i, j) == potion.get_pos():
                        sc.blit(potion.image, (cell_size * i, cell_size * j))
        # рисуем полостку здоровья
        pygame.draw.rect(sc, pygame.Color('red'), (0, HEIGHT - 10, hero.health * 10, HEIGHT))
        if hero.get_is_inventory_print:
            pygame.draw.line(sc, (255, 0, 0), (1200, 0), (1200, 800), 2)
        all_sprites.draw(sc)
        character_sprites.draw(sc)
        pygame.display.flip()
    clock.tick(FPS)
