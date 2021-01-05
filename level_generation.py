import pygame
from Items import *
from functions import sc, texture_wall, texture_floor, character_sprites

# количество предметов на каждом уровне - монстры, оружие,броня, зелья
level1 = [5, 6, 5, 8]
level2 = [7, 3, 4, 5]
level3 = [10, 1, 2, 3]
# текущий уровень
cur_level = 1
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


def draw_map():
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
