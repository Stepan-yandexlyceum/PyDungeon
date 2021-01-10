import pygame
from player import Player
from map import *
from music_player import *
from level_generation import *

pygame.init()

# установка количества кадров в секунду
clock = pygame.time.Clock()

# создадим игрока
hero = Player(sc, character_sprites)

running = True

# создаем карту

# основной цикл отрисовки
start = False
play_music("data\music\main_theme.mp3")
start_screen()
generate_new_level()
while running:
    sc.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # сохраняем предыдущую позицию игрока
            prev_pos = (hero.x, hero.y)
            hero.movement()
            step_sound()
            hero.print_inventory()
            # проверяем на столкновения с предметами
            for enemy in enemies:
                if (hero.x, hero.y) == enemy.get_pos():
                    print("hit")
                    # откатываем игрока на предыдущую клетку
                    hero.x, hero.y = prev_pos
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
                    # hero.add_inventory(weapon)
                    hero.weapon = weapon
                    inventory_sound("weapon")
                    add_to_log("Ты подобрал {}".format(weapon.name))
                    add_to_log("Оно имеет {} урона".format(weapon.damage))
                    weapons.remove(weapon)
            for arm in armor:
                if (hero.x, hero.y) == arm.get_pos():
                    # hero.add_inventory(arm)
                    hero.armor = arm
                    inventory_sound()
                    add_to_log("Ты подобрал {}".format(arm.name))
                    add_to_log("Оно блокирует {} урона".format(arm.defence))
                    armor.remove(arm)
            for potion in potions:
                if (hero.x, hero.y) == potion.get_pos():
                    # hero.add_inventory(potion)
                    inventory_sound()
                    add_to_log("Ты подобрал {}".format(potion.name))
                    if potion.name == "Small_health":
                        if hero.health + 5 <= hero.max_health:
                            hero.health += 5
                        else:
                            hero.health = hero.max_health
                        add_to_log("Оно восстанавливает 5 ед. здоровья")
                    elif potion.name == "Small_strength":
                        hero.max_health += 5
                        hp_bar = pygame.transform.scale(hp_bar, (hero.max_health * 10, 20))
                        add_to_log("Оно увеличивает максимальный запас здоровья на 5 ед.")
                    potions.remove(potion)
    # проверяем здоровье игрока
    if hero.health <= 0:
        gameover_screen()
        running = False
        terminate()
    if hero.x >= map_width - 1:
        door_sound()
        level2_screen()
        cur_level += 1
        # map_width += 4
        # map_height += 4
        # заново генерируем лабиринт
        print("new level")
        text_map = map_generation(map_width, map_height)
        generate_new_level()
        hero.x, hero.y = 1, 1
        # break
    draw_map()
    # рисуем игрока
    for i in range(map_height):
        for j in range(map_width):
            if (i, j) == (hero.x, hero.y):
                sc.blit(hero.image, (cell_size * i, cell_size * j))
    # рисуем полостку здоровья
    pygame.draw.rect(sc, pygame.Color('red'), (10, HEIGHT - 20, 10 + hero.health * 10, 10))
    sc.blit(hp_bar, (0, HEIGHT - 25, 200, 10))
    # рисуем экипированные предметы
    sc.blit(hero.image, (0, HEIGHT - 100, cell_size, cell_size))
    sc.blit(frame, (0, HEIGHT - 100, cell_size, cell_size))
    if hero.weapon:
        sc.blit(hero.weapon.image, (cell_size, HEIGHT - 100, cell_size, cell_size))
    sc.blit(frame, (cell_size, HEIGHT - 100, cell_size, cell_size))
    if hero.armor:
        sc.blit(hero.armor.image, (cell_size * 2, HEIGHT - 100, cell_size, cell_size))
    sc.blit(frame, (cell_size * 2, HEIGHT - 100, cell_size, cell_size))
    if hero.get_is_inventory_print:
        pygame.draw.line(sc, (255, 0, 0), (1200, 0), (1200, 800), 2)
    all_sprites.update()
    all_sprites.draw(sc)
    print_log()
    # character_sprites.draw(sc)
    if hero.health < 5:
        sc.blit(blood_screen, (0, 0))
    pygame.display.flip()
    clock.tick(FPS)
