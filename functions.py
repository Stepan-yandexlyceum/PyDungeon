import os
import sys
import pygame
from settings import *

sc = pygame.display.set_mode((WIDTH, HEIGHT))
# текущий уровень
cur_level = 1


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if cur_level == 1:
    texture_wall = load_image("image/Brick_Wall_009.jpg")
elif cur_level == 2:
    texture_wall = load_image("image/stone_wall2.png")
else:
    texture_wall = load_image("image/wall3.jpg")
texture_wall = pygame.transform.scale(texture_wall, (cell_size * 2, cell_size * 2))
texture_floor = load_image("image/dark-brick-wall-texture_1048-7626.jpg")
texture_floor = pygame.transform.scale(texture_floor, (cell_size, cell_size))
hp_bar = load_image("image/hud/frame.png")
hp_bar = pygame.transform.scale(hp_bar, (240, 20))
door = load_image("image/castledoors.png")
door = pygame.transform.scale(door, (cell_size, cell_size))
# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()
character_sprites = pygame.sprite.Group()


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


def level2_screen():
    intro_text = ["ВЫ СМОГЛИ ПРОЙТИ ПЕРВЫЙ УРОВЕНЬ ПОДЗЕМЕЛЬЯ",
                  "но это еще не конец...",
                  "Впереди Вас ждут еще более сильные противники",
                  "и гораздо меньше шансов на выживание"]

    fon = pygame.transform.scale(load_image('image/level2_dungeon.jpg'), (WIDTH, HEIGHT))
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


def level3_screen():
    intro_text = ["НЕМНОГИЕ ЗАХОДИЛИ ТАК ДАЛЕКО",
                  "И еще никто не возвращался",
                  "С последнего, самого мрачного и глубокого уровня",
                  "Смельчак ли ты или безумец?"]

    fon = pygame.transform.scale(load_image('image/level3_dungeon.jpg'), (WIDTH, HEIGHT))
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
