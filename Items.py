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

    def get_type(self):
        return self.type


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
        self.x, self.y = 0, 0

    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage

    def get_pos(self):
        return self.x, self.y

    def generate_pos(self):
        # генерируем положение монстра
        self.x, self.y = random.choice(list_corridors)  # тут нужна еще проверка на то что клетка занята


weapon_lib = {
    "Меч": 5,
    "Булава": 4,
    "Посох": 3}
