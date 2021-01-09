import pygame
from Items import *
from functions import sc, texture_floor, character_sprites, cur_level

# количество предметов на каждом уровне - монстры, оружие,броня, зелья
level1 = [5, 6, 5, 8]
level2 = [7, 3, 4, 5]
level3 = [10, 1, 2, 3]
all_levels = [level1, level2, level3]
# добавляем объекты на карте
# добавляем врагов
enemies = []
weapons = []
armor = []
potions = []


def generate_new_level():
    for i in range(all_levels[cur_level - 1][0]):
        monster = Enemy('enemy', random.choice(["Ghost", "Minotaur", "Golem"]), character_sprites)
        enemies.append(monster)
    # добавляем оружие
    for i in range(all_levels[cur_level - 1][1]):
        weapon = Weapon('weapon', random.choice(["Double_Axe", "Hammer", "Stick", "Sword"]), character_sprites)
        weapons.append(weapon)
    for i in range(all_levels[cur_level - 1][2]):
        arm = Armor('armor', random.choice(["Helmet1", "Helmet2", "Cuiras1", "Cuiras2", "Arm_armor1", "Arm_armor2",
                                            "Leg_armor1", "Leg_armor2"]), character_sprites)
        armor.append(arm)
    for i in range(level1[3]):
        potion = Potion('potion', random.choice(["Small_health", "Small_strength"]), character_sprites)
        potions.append(potion)


def draw_map():
    texture_wall = update_wall_color()
    # рисуем карту
    for i in range(map_height):
        for j in range(map_width):
            if text_map[i][j] == 'w':
                sc.blit(texture_wall, (cell_size * i, cell_size * j))
            if text_map[i][j] == 'c':
                sc.blit(texture_floor, (cell_size * i, cell_size * j))
            if text_map[i][j] == 'c' and i == map_width - 1:
                sc.blit(door, (cell_size * i, cell_size * j))
    # рисуем монстров
    for enemy in enemies:
        sc.blit(enemy.image, (cell_size * enemy.x, cell_size * enemy.y))
    # рисуем оружие
    for weapon in weapons:
        sc.blit(weapon.image, (cell_size * weapon.x, cell_size * weapon.y))
    # рисуем броню
    for arm in armor:
        sc.blit(arm.image, (cell_size * arm.x, cell_size * arm.y))
    # рисуем зелья
    for potion in potions:
        sc.blit(potion.image, (cell_size * potion.x, cell_size * potion.y))
