import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, weapon, armor, sprites_group):
        super().__init__(sprites_group)
        self.weapon = weapon
        self.armor = armor
        self.x = 0  # TODO: генерировать это в соответствии с условиями
        self.y = 0

    @property
    def pos(self):
        return self.x, self.y
