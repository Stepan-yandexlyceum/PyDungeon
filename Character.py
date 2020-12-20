import pygame


class Character:
    def __init__(self, weapon, armor):
        self.weapon = weapon
        self.armor = armor
        self.x = 0 # TODO: генерировать это в соответствии с условиями
        self.y = 0

    @property
    def pos(self):
        return self.x, self.y