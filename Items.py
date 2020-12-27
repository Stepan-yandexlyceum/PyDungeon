import pygame
import random
from main import load_image
from settings import *
from map import map_width, map_height, list_corridors


# тут собраны все предметы и существа, которые могут встретиться в подземелье
# type это тип предмета, enemy - враг, weapon - оружие, potion - зелье
class Item(pygame.sprite.Sprite):
    def __init__(self, type, name, sprites_group):
        super().__init__(sprites_group)
        self.type = type
        self.name = name
        self.x, self.y = 0, 0

    def get_type(self):
        return self.type

    def get_pos(self):
        return self.x, self.y

    def generate_pos(self):
        # генерируем положение монстра
        self.x, self.y = random.choice(list_corridors)
        # удаляем занятое поле
        for i in range(list_corridors):
            if list_corridors[i] == (self.x, self.y):
                list_corridors.pop(i)


class Enemy(Item):
    # название: [урон, здоровье, картинка]
    enemy_lib = {
        "Ghost": [5, 8, "Wraith_01_Idle_000.png"],
        "Minotaur": [4, 15, "Minotaur_01_Idle_000.png"],
        "Golem": [7, 20, "Golem_01_Idle.png"]
    }

    def __init__(self, type, name, sprites_group):
        super().__init__(type, name, sprites_group)
        # определяем характеристики по имени монстра
        self.health = Enemy.enemy_lib[name][0] + random.randint(-2, 2)  # делаем небольшой разброс по характеристикам
        self.damage = Enemy.enemy_lib[name][1] + random.randint(-2, 2)
        self.image = load_image(Enemy.enemy_lib[name][0])
        self.image = pygame.transform.scale(self.image, cell_size)

    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage

    def remove(self):
        # смерть
        # -1 означает, что эти предметы отрисовывать не надо
        self.health = -1
        self.damage = -1
        self.x, self.y = -1, -1
        list_corridors.append((self.x, self.y))


class Weapon(Item):
    weapon_lib = {
        "Меч": 5,
        "Булава": 4,
        "Посох": 3}

    def __init__(self, type, name, sprites_group):
        super().__init__(type, name, sprites_group)
        self.damage = Weapon.weapon_lib[name] + random.randint(-2, 2)

    def get_damage(self):
        return self.damage

    def remove(self):
        list_corridors.append((self.x, self.y))


class Potion(Item):
    # тут мало свойств тк у каждого зелья свой эффект
    potion_lib = {
        "Small_health": [3, "small_health_potion.png"],
        "Булава": [3, "small_strength_potion.png"],
        "Посох": [3, "icon27.png"]}

    def __init__(self, type, name, sprites_group):
        super().__init__(type, name, sprites_group)
        self.image = load_image(Potion.potion_lib[name][1])
        self.image = pygame.transform.scale(self.image, cell_size)

    def get_name(self):
        return self.name
