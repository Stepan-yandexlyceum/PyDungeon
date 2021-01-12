import pygame
import os
import sys
from settings import *
from player import *
from map import *
from music_player import *
from level_generation import *

pygame.init()

# установка количества кадров в секунду
clock = pygame.time.Clock()

# создадим игрока
hero = Player(sc, character_sprites)

draw_player_in_inventory()
button_del = Button(1300, 600, 100, 30, 'удалить')
button_use = Button(1275, 650, 150, 30, 'использовать')

hero = Player(sc, character_sprites)
cur_level = 1
running = True

# создаем карту

# основной цикл отрисовки
start = False
#play_music("data\music\main_theme.mp3")
start_screen()
generate_new_level(cur_level)
while running:
    sc.fill((0, 0, 0))
    inventory = hero.get_inventory()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            inventory.get_click(event.pos)
            if button_del.push_button(event.pos):
                inventory.clear_cell()
            if button_use.push_button(event.pos):
  
                if inventory.get_selected_cell() != ('', '') and inventory.board[inventory.selected_cell[0]][inventory.selected_cell[1]] != '':
                    obj = inventory.get_selected_cell()
                    if obj.get_type() == "weapon":
                        old_w = hero.replace_weapon(obj)
                        inventory.board[inventory.selected_cell[0]][inventory.selected_cell[1]] = old_w

                    if obj.get_name() == "Helmet1" or obj.get_name() == 'Helmet2':
                        old_w = hero.replace_helmet(obj)
                        inventory.board[inventory.selected_cell[0]][inventory.selected_cell[1]] = old_w
                    
                    if obj.get_name() == "Cuiras1" or obj.get_name() == 'Cuiras2':
                        old_w = hero.replace_armor(obj)
                        inventory.board[inventory.selected_cell[0]][inventory.selected_cell[1]] = old_w

                    if obj.get_name() == "Leg_armor1" or obj.get_name() == 'Leg_armor1':
                        old_w = hero.replace_leg(obj)
                        inventory.board[inventory.selected_cell[0]][inventory.selected_cell[1]] = old_w

                    if obj.get_type() == "potion":

                        if obj.get_name() == "Small_health":
                            if hero.health + 5 <= hero.max_health:
                                hero.health += 5
                            else:
                                hero.health = hero.max_health
                        elif potion.name == "Small_strength":
                            hero.max_health += 5
                        inventory.clear_cell()
                        print(inventory.board[inventory.selected_cell[0]][inventory.selected_cell[1]])
                        
        if event.type == pygame.KEYDOWN:
            # сохраняем предыдущую позицию игрока
            prev_pos = (hero.x, hero.y)
            hero.movement()
            #step_sound()
            hero.print_inventory()
            # проверяем на столкновения с предметами
            for enemy in enemies:
                if (hero.x, hero.y) == enemy.get_pos():
                    print("hit")
                    # откатываем игрока на предыдущую клетку
                    #hero.x, hero.y = prev_pos
                    character_sprites.draw(sc)

                    # если у героя есть броня
                    if hero.armor:
                        if enemy.damage <= hero.armor.defence:
                            hero.health -= (enemy.damage - hero.armor.defence)
                            add_to_log("Тебя ударил {}".format(enemy.name))
                        else:
                            add_to_log("Тебя ударил {}, но твоя броня слишком крепкая,".format(enemy.name))
                            add_to_log("поэтому ты не получил урона")
                    else:
                        hero.health -= enemy.damage
                        add_to_log("Тебя ударил {}".format(enemy.name))
                    # если у героя есть оружие
                    if hero.weapon:
                        enemy.health -= hero.weapon.get_damage()
                        add_to_log("Ты ударил {}, используя {}".format(enemy.name, hero.weapon.name))
                    else:
                        enemy.health -= 2
                        add_to_log("Ты ударил {}, используя руку".format(enemy.name))
                    # рисуем здоровье противника
                    # pygame.draw.rect(sc, pygame.Color('black'),
                    #                  (enemy.x * cell_size, enemy.y * cell_size + cell_size, cell_size, 3))
                    # pygame.draw.rect(sc, pygame.Color('red'),
                    #                  (enemy.x * cell_size, enemy.y * cell_size + cell_size, enemy.health, 3))
                    if enemy.health <= 0:
                        enemy.kill()
                        enemies.remove(enemy)
                    injure_sound()
                    # TODO: можно настроить область распространения частиц
                    screen_rect = (hero.x * cell_size, hero.y * cell_size, hero.x * cell_size + cell_size,
                                   hero.y * cell_size + cell_size)
                    create_particles((hero.x * cell_size, hero.y * cell_size), screen_rect)

                    break
            # TODO: добавить в класс игрока метод add_inventory(item) для добавления предмета в инвентарь
            for weapon in weapons:
                if (hero.x, hero.y) == weapon.get_pos():
                    if hero.weapon == '':
                        hero.weapon = weapon
                    else:
                        inventory.add_object(weapon)
                    inventory_sound("weapon")
                    add_to_log("Ты подобрал {}".format(weapon.name))
                    add_to_log("Оно имеет {} урона".format(weapon.damage))
                    weapons.remove(weapon)
            for arm in armor:
                if (hero.x, hero.y) == arm.get_pos():
                    inventory_sound()
                    inventory.add_object(arm)
                    add_to_log("Ты подобрал {}".format(arm.name))
                    add_to_log("Оно блокирует {} урона".format(arm.defence))
                    armor.remove(arm)
            for potion in potions:
                if (hero.x, hero.y) == potion.get_pos():
                    # hero.add_inventory(potion)
                    inventory_sound()
                    inventory.add_object(potion)
                    add_to_log("Ты подобрал {}".format(potion.name))
                    if potion.name == "Small_health":
                        add_to_log("Оно восстанавливает 5 ед. здоровья")
                    elif potion.name == "Small_strength":
                        hp_bar = pygame.transform.scale(hp_bar, (hero.max_health * 10, 20))
                        add_to_log("Оно увеличивает максимальный запас здоровья на 5 ед.")
                    potions.remove(potion)
    # проверяем здоровье игрока
    if hero.health <= 0:
        gameover_screen()
        running = False
        terminate()
    if hero.x >= map_width - 1:
        #door_sound()
        level2_screen()
        cur_level += 1
        # map_width += 4
        # map_height += 4
        # заново генерируем лабиринт
        print("new level")
        text_map = map_generation(map_width, map_height)
        generate_new_level(cur_level)
        hero.x, hero.y = 1, 1
        player_pos = (1, 1)
        # break
    draw_map(cur_level)
    # рисуем игрока
    for i in range(map_height):
        for j in range(map_width):
            if (i, j) == (hero.x, hero.y):
                sc.blit(hero.image, (cell_size * i, cell_size * j))
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

    # рисуем экипированные предметы
    sc.blit(hero.image, (0, HEIGHT - 100, cell_size, cell_size))
    sc.blit(frame, (0, HEIGHT - 100, cell_size, cell_size))
    if hero.weapon:
        sc.blit(hero.weapon.image, (cell_size, HEIGHT - 100, cell_size, cell_size))
        sc.blit(hero.weapon.image, (1250, 30))
    sc.blit(frame, (cell_size, HEIGHT - 100, cell_size, cell_size))
    if hero.armor:
        sc.blit(hero.armor.image, (cell_size * 2, HEIGHT - 100, cell_size, cell_size))
        sc.blit(hero.armor.image, (1250, 63))
    if hero.helmet:
        sc.blit(hero.helmet.image, (1418, 30))

    if hero.leg:
        sc.blit(hero.leg.image, (1418, 63))

    sc.blit(frame, (cell_size * 2, HEIGHT - 100, cell_size, cell_size))
    if hero.get_is_inventory_print:
        pygame.draw.line(sc, (255, 0, 0), (1200, 0), (1200, 800), 2)
    hero.print_inventory()
    all_sprites.update()
    all_sprites.draw(sc)
    print_log()
    # character_sprites.draw(sc)
    if hero.health < 5:
        sc.blit(blood_screen, (0, 0))

    hero.inventory = inventory
    
    pygame.display.flip()
    clock.tick(FPS)
