import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, weapon, armor, helmet, leg, sprites_group):
        super().__init__(sprites_group)
        self.weapon = weapon
        self.armor = armor
        self.helmet = helmet
        self.leg = leg
        self.x = 0
        self.y = 0

    @property
    def pos(self):
        return self.x, self.y
