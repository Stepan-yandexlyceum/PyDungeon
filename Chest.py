import pygame
from map import list_corridors
from random import choice
import settings


class Chest(pygame.sprite.Sprite):
    image = pygame.image.load("data/image/reinforced_wood.jpg")

    def __init__(self, coord, sprites_grop):
        super().__init__(sprites_grop)
        self.image = Chest.image
        self.x, self.y = coord
        self.rect = pygame.Rect(self.x * 32 + 5, self.y * 32 + 5, 22, 22)


def generation_chest(num_chest, sprites_grop):
    coords_chest = []
    for i in range(num_chest):
        coord = choice(list_corridors)
        if coord in coords_chest:
            num_chest += 1
        else:
            coords_chest.append(coord)
            Chest(coord, sprites_grop)
    