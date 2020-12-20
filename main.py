import pygame
import os
import sys
from settings import *
from player import Player
from map import text_map
from Character import Character
from Armor import Armor
from Enemy import Enemy
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
# установка количества кадров в секунду
clock = pygame.time.Clock()
# создание игрока
#player = Player()

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()

# создадим спрайт
player_sprite = pygame.sprite.Sprite()
# определим его вид
player_sprite.image = load_image("Knight_01__IDLE_000.png")
# и размеры
# TODO: подогнать спрайт игрока под сетку и отрегулировать перемещение в квадратиках
player_sprite.image = pygame.transform.scale(player_sprite.image, (100, 100))
player_sprite.rect = player_sprite.image.get_rect()

# добавим спрайт в группу
all_sprites.add(player_sprite)

running = True
# основной цикл отрисовки
while True:
    for event in pygame.event.get():
        sc.fill((0, 0, 0))
        a, b = 0, 0
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.MOUSEMOTION:
        #     x, y = event.pos[0], event.pos[1]
        #     screen.fill((0, 0, 0))
        #     sprite.rect.x = x
        #     sprite.rect.y = y
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_sprite.rect.y += -10
            if event.key == pygame.K_a:
                player_sprite.rect.x += -10
            if event.key == pygame.K_s:
                player_sprite.rect.y += 10
            if event.key == pygame.K_d:
                player_sprite.rect.x += 10

    all_sprites.draw(sc)
    pygame.display.flip()
    # TODO: отраисовывать карту и игрока в ней
    clock.tick(FPS)
