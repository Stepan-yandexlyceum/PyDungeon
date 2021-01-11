import pygame
import os
import sys
from settings import *
from player import *
from map import *
from Character import Character
from Items import *
from functions import *
from random import choices
from music_player import play_music, injure_sound, door_sound
from level_generation import *

pygame.init()

# установка количества кадров в секунду
clock = pygame.time.Clock()

hammer = Weapon("Hammer", "Hammer", all_sprites)
legs = Armor("Leg_armor1", "Leg_armor1", all_sprites)

# создадим игрока
hero = Player(sc, character_sprites, weapon=hammer, leg=legs)

draw_player_in_inventory()
button_del = Button(1300, 600, 100, 30, 'удалить')
button_use = Button(1275, 650, 150, 30, 'использовать')

running = True

# создаем карту
text_map = map_generation(map_width, map_height)
list_corridors = get_corridors(text_map)

# основной цикл отрисовки
start = False
#play_music("data\music\main_theme.mp3")
start_screen()

while running:
    sc.fill((0, 0, 0))
    inventory = hero.get_inventory()
    for event in pygame.event.get():
        sc.fill((0, 0, 0))
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            inventory.get_click(event.pos)
            if button_del.push_button(event.pos):
                inventory.clear_cell()
            if button_use.push_button(event.pos):
                if inventory.get_selected_cell() != "":
                    obj = inventory.get_selected_cell()
                    if obj is Weapon:
                        old_w = hero.get_weapon()
                        
        if event.type == pygame.KEYDOWN:
            # сохраняем предыдущую позицию игрока
            prev_pos = (hero.x, hero.y)
            hero.movement()
            hero.print_inventory()
            # проверяем на столкновения с предметами
            for enemy in enemies:
                if (hero.x, hero.y) == enemy.get_pos():
                    print("hit")
                    # откатываем игрока на предыдущую клетку
                    # TODO: откат персонажа
                    # hero.x, hero.y = prev_pos
                    character_sprites.draw(sc)

                    # если у героя есть броня
                    if hero.armor:
                        hero.health -= (enemy.damage - hero.armor.defence)
                    else:
                        hero.health -= enemy.damage
                    # если у героя есть оружие
                    if hero.weapon:
                        enemy.health -= hero.weapon.damage
                    else:
                        enemy.health -= 2
                    if enemy.health <= 0:
                        enemy.kill()
                    injure_sound()
                    # TODO: можно настроить область распространения частиц
                    screen_rect = (hero.x * cell_size, hero.y * cell_size, hero.x * cell_size + cell_size,
                                   hero.y * cell_size + cell_size)
                    create_particles((hero.x * cell_size, hero.y * cell_size), screen_rect)

                    break
            # TODO: добавить в класс игрока метод add_inventory(item) для добавления предмета в инвентарь
            for weapon in weapons:
                if (hero.x, hero.y) == weapon.get_pos():
                    inventory.add_object(weapon)
                    weapons.remove(weapon)
            for arm in armor:
                if (hero.x, hero.y) == arm.get_pos():
                    inventory.add_object(arm)
                    armor.remove(arm)
            for potion in potions:
                if (hero.x, hero.y) == potion.get_pos():
                    inventory.add_object(potion)
                    potions.remove(potion)
    # проверяем здоровье игрока
    if hero.health <= 0:
        running = False

    if hero.x >= map_width - 1:
        #door_sound()
        level2_screen()
        cur_level += 1
        # map_width += 4
        # map_height += 4
        # заново генерируем лабиринт
        print("new level")
        new_map()
        hero.x, hero.y = 1, 1
        player_pos = (1, 1)
        # break
    draw_map()

    # рисуем полостку здоровья
    pygame.draw.rect(sc, pygame.Color('red'), (10, HEIGHT - 20, 10 + hero.health * 10, 10))
    sc.blit(hp_bar, (0, HEIGHT - 25, 200, 10))

    if hero.get_is_inventory_print():
        pygame.draw.line(sc, (255, 255, 255), (1200, 0), (1200, 800), 2)
        pygame.draw.rect(sc, (255, 255, 255), (1250, 30, 33, 33), width=1)
        pygame.draw.rect(sc, (255, 255, 255), (1250, 62, 33, 33), width=1)
        pygame.draw.rect(sc, (255, 255, 255), (1417, 30, 33, 33), width=1)
        pygame.draw.rect(sc, (255, 255, 255), (1417, 62, 33, 33), width=1)
        
        inventory.render(sc)
        inventory.underline_selected_cell()

    button_del.draw()
    button_use.draw()

    # TODO: fix this
    all_sprites.update()
    all_sprites.draw(sc)

    inventory_sprites.update()
    inventory_sprites.draw(sc)

    equipment_sprites.update()
    equipment_sprites.draw(sc)

    character_sprites.update()
    character_sprites.draw(sc)
    if hero.health < 5:
        sc.blit(blood_screen, (0, 0))

    hero.inventory = inventory
    
    pygame.display.flip()
    clock.tick(FPS)
