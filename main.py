import pygame
import os
import sys
from settings import *
from Chest import *
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


texture_wall = load_image("image/textures_dungeon_001.png")
texture_floor = load_image("image/dark-brick-wall-texture_1048-7626.jpg")
texture_floor = pygame.transform.scale(texture_floor, (32, 32))
# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()
character_sprites = pygame.sprite.Group()
# создадим начальное снаряжение для игрока (потом переденесем в БД, но потом)
wooden_baton = Weapon("деревянная дубина", 3, 2)
leather_cuirass = Armor("кожаная кираса", 0, 1)

# создадим игрока
hero = Player(wooden_baton, leather_cuirass, sc, character_sprites)

running = True
# основной цикл отрисовки
start = False
start_screen()

generation_chest(5, all_sprites)

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
                    sc.blit(texture_wall, (32 * i, 32 * j))
                if text_map[i][j] == 'c':
                    sc.blit(texture_floor, (32 * i, 32 * j))
        all_sprites.draw(sc)
        character_sprites.draw(sc)
        pygame.display.flip()
    clock.tick(FPS)
