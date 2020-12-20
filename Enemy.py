import pygame
from Character import *
import random

# название: [урон, здоровье]
# название врагов можно откорректировать в зависимости от спрайтов которые найдем
# пока в data лежат спрайты к этим:
enemy_lib = {
    "Призрак": [5, 8],
    "Минотавр": [4, 15],
    "Голем": [7, 20]
}


class Enemy(Character):
    def __init__(self, weapon, armor):
        super().__init__(weapon, armor)
        self.name = ""
        self.health = 0
        self.damage = 0

    def generate(self):
        # генерим случайного монстра из словаря
        rand = random.choice(["Призрак", "Минотавр", "Голем"])
        self.name = rand
        self.health = enemy_lib[rand][1]
        self.damage = enemy_lib[rand][0]
        # TODO: генерить x,y монстра в случайной незанятой клетке.