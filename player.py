from Items import *
from map import text_map
from functions import *
from settings import *
from Character import *
import pygame


class Player(Character):
    image = pygame.image.load("data/image/knight.png")
    image = pygame.transform.scale(image, (cell_size, cell_size))

    def __init__(self, screen, sprites, weapon="", armor="", helmet="", leg=""):
        super().__init__(weapon, armor, helmet, leg, sprites)
        self.x, self.y = player_pos
        self.rect = pygame.Rect(self.x * cell_size, self.y * cell_size, cell_size, cell_size)
        self.direction = 'right'
        self.health = 20

        self.inventory = Board_Inventory()
        self.is_inventory_print = False

    def pos(self):
        return self.x, self.y

    def get_health(self):
        return self.health

    def movement(self):
        keys = pygame.key.get_pressed()

        y = self.rect.y
        x = self.rect.x
        m_y = self.y
        m_x = self.x
        # управление игроком производится клавишами w,a,s,d
        if keys[pygame.K_w]:
            self.rect.y += -cell_size
            self.y -= 1
        if keys[pygame.K_a]:
            self.rect.x -= cell_size
            self.x -= 1
            self.flip_image('left')
        if keys[pygame.K_s]:
            self.rect.y += cell_size
            self.y += 1
        if keys[pygame.K_d]:
            self.rect.x += cell_size
            self.x += 1
            self.flip_image('right')

        if keys[pygame.K_DOWN]:
            self.rect.y += cell_size
            self.y += 1
        if keys[pygame.K_LEFT]:
            self.rect.x -= cell_size
            self.x -= 1
            self.flip_image('left')
        if keys[pygame.K_UP]:
            self.rect.y -= cell_size
            self.y -= 1
        if keys[pygame.K_RIGHT]:
            self.rect.x += cell_size
            self.x += 1
            self.flip_image('right')

        if text_map[self.x][self.y] == 'w':
            self.rect.y = y
            self.rect.x = x
            self.y = m_y
            self.x = m_x

    def flip_image(self, direction):
        if direction != self.direction:
            self.image = pygame.transform.flip(self.image, True, False)
            if self.direction == 'right':
                self.direction = 'left'
            else:
                self.direction = 'right'

    def get_is_inventory_print(self):
        return self.is_inventory_print

    def get_inventory(self):
        return self.inventory

    def print_inventory(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_e]:
            if self.is_inventory_print:
                sc = pygame.display.set_mode((WIDTH, HEIGHT))
            else:
                sc = pygame.display.set_mode((WIDTH_MAP_AND_INVENTORY, HEIGHT))
                if self.weapon != '':
                    weapon_sprite = pygame.sprite.Sprite()
                    weapon_sprite.image = self.weapon.get_image()
                    weapon_sprite.image = pygame.transform.scale(weapon_sprite.image, (30, 30))
                    weapon_sprite.rect = weapon_sprite.image.get_rect()
                    weapon_sprite.rect.x = 1250
                    weapon_sprite.rect.y = 30
                    equipment_sprites.add(weapon_sprite)

                if self.armor != '':
                    armor_sprite = pygame.sprite.Sprite()
                    armor_sprite.image = self.armor.get_image()
                    armor_sprite.rect = weapon_sprite.image.get_rect()
                    armor_sprite.image = pygame.transform.scale(armor_sprite.image, (30, 30))
                    armor_sprite.rect.x = 1250
                    armor_sprite.rect.y = 63
                    equipment_sprites.add(armor_sprite)

                if self.helmet != '':
                    helmet_sprite = pygame.sprite.Sprite()
                    helmet_sprite.image = self.helmet.get_image()
                    helmet_sprite.rect = weapon_sprite.image.get_rect()
                    helmet_sprite.image = pygame.transform.scale(helmet_sprite.image, (30, 30))
                    helmet_sprite.rect.x = 1418
                    helmet_sprite.rect.y = 30
                    equipment_sprites.add(helmet_sprite)

                if self.leg != '':
                    leg_sprite = pygame.sprite.Sprite()
                    leg_sprite.image = self.leg.get_image()
                    leg_sprite.rect = weapon_sprite.image.get_rect()
                    leg_sprite.image = pygame.transform.scale(leg_sprite.image, (30, 30))
                    leg_sprite.rect.x = 1418
                    leg_sprite.rect.y = 63
                    equipment_sprites.add(leg_sprite)

            self.is_inventory_print = not self.is_inventory_print

    def get_armor(self):
        if self.armor is Armor:
            return self.armor

    def get_helmet(self):
        if self.helmet is Armor:
            return self.helmet

    def get_leg(self):
        if self.leg is Armor:
            return self.leg

    def get_weapon(self):
        if self.weapon is Weapon:
            return self.weapon

    def replace_armor(self, armor):
        if armor is Armor:
            answer = self.armor
            self.armor = armor
            return answer
        return ''

    def replace_helmet(self, helmet):
        if helmet is Armor:
            answer = self.helmet
            self.helmet = helmet
            return answer
        return ''

    def replace_leg(self, leg):
        if leg is Armor:
            answer = self.leg
            self.leg = leg
            return answer
        return ''

    def replace_weapon(self, weapon):
        if weapon is Weapon:
            answer = self.weapon
            self.weapon = weapon
            return answer
        return ''



class Board_Inventory:
    def __init__(self):
        self.width = 4
        self.height = 5
        self.board = [[""] * self.height for i in range(self.width)]
        self.left = 1286
        self.top = 300
        self.cell_size = 32
        self.selected_cell = ("", "")
        

    def render(self, screen):
        for i in range(0, self.height * self.cell_size, self.cell_size):
            for j in range(0, self.width * self.cell_size, self.cell_size):
                pygame.draw.rect(screen, pygame.Color('white'), (
                    j + self.left, i + self.top, self.cell_size, self.cell_size
                ), 1)

    def get_cell(self, mouse_pos):
        height = self.top + self.height * self.cell_size
        widht = self.left + self.width * self.cell_size
        if widht > mouse_pos[0] and mouse_pos[1] > self.top and height > mouse_pos[1] and mouse_pos[0] > self.left:
            height_answer = int((mouse_pos[1] - self.top) / self.cell_size)
            widht_answer = int((mouse_pos[0] - self.left) / self.cell_size)
            return widht_answer, height_answer
        else:
            return None

    def on_click(self, cell_coords):
        self.selected_cell = cell_coords

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell != None:
            self.on_click(cell)

    def clear_cell(self):
        if self.selected_cell != ("", "") and self.board[self.selected_cell[0]][self.selected_cell[1]] != "":
            self.board[self.selected_cell[0]][self.selected_cell[1]].kill()
            inventory_sprites.remove(self.board[self.selected_cell[0]][self.selected_cell[1]])
            self.board[self.selected_cell[0]][self.selected_cell[1]] = ""

    def underline_selected_cell(self):
        if self.selected_cell != ("", ""):
            pygame.draw.rect(sc, (255, 0, 0), (self.left + self.selected_cell[0] * 32, self.top + self.selected_cell[1] * 32, 32, 32), 1)

    def add_object(self, obj):
        for i in range(self.width):
            for ii in range(self.height):
                if self.board[i][ii] == "":
                    self.board[i][ii] = obj
                    sprite = pygame.sprite.Sprite()
                    sprite.image = self.board[i][ii].get_image()
                    sprite.rect = sprite.image.get_rect()
                    sprite.image = pygame.transform.scale(sprite.image, (30, 30))
                    sprite.rect.x = self.left + i * 32
                    sprite.rect.y = self.top + ii * 32
                    inventory_sprites.add(sprite)
                    return

    def get_selected_cell(self):
        if self.selected_cell != ("", "") and self.board[self.selected_cell[0]][self.selected_cell[1]] != "":
            return self.board[self.selected_cell[0]][self.selected_cell[1]]
        return ""


class Button:
    def __init__(self, x, y, height, width, text):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.text = text

    def draw(self):
        pygame.draw.rect(sc, (255, 255, 255), (self.x, self.y, self.height, self.width), width=1)

        font = pygame.font.Font(None, self.width)
        text = font.render(self.text, True, (255, 255, 255))
        sc.blit(text, (self.x + 5, self.y + 5))

    def push_button(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.height and pos[1] > self.y and pos[1] < self.y + self.width:
            return True
            



def draw_player_in_inventory():
    hero_in_inventory = pygame.sprite.Sprite()
    hero_in_inventory.image = load_image("image\knight.png")
    hero_in_inventory.image = pygame.transform.scale(hero_in_inventory.image, (100, 100))

    hero_in_inventory.rect = hero_in_inventory.image.get_rect()

    hero_in_inventory.rect.x = 1300
    hero_in_inventory.rect.y = 0

    all_sprites.add(hero_in_inventory)