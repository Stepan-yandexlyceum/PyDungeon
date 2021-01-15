import os
import sys
import pygame
from settings import *
import random
import sqlite3

sc = pygame.display.set_mode((WIDTH, HEIGHT))
# текущий уровень
all_logs = []


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def add_to_log(text):
    all_logs.append(text)
    if len(all_logs) > 20:
        del all_logs[0]


def draw_white_rect(x, y):
    pygame.draw.rect(sc, (255, 255, 255), (x, y, 50, 50), width=1)


def print_log():
    font = pygame.font.Font(None, 25)
    text_coord = 25
    for line in all_logs:
        string_rendered = font.render(line, 1, pygame.Color('yellow'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 725
        text_coord += intro_rect.height
        sc.blit(string_rendered, intro_rect)


def update_wall_color(cur_level):
    if cur_level == 1:
        texture_wall = load_image("image/Brick_Wall_009.jpg")
        texture_wall = pygame.transform.scale(texture_wall, (cell_size * 2, cell_size * 2))
    elif cur_level == 2:
        texture_wall = load_image("image/stone_wall2.png")
        texture_wall = pygame.transform.scale(texture_wall, (cell_size * 2, cell_size * 2))
    else:
        texture_wall = load_image("image/wall3.jpg")
        texture_wall = pygame.transform.scale(texture_wall, (cell_size * 2, cell_size * 2))
    return texture_wall


texture_floor = load_image("image/dark-brick-wall-texture_1048-7626.jpg")
texture_floor = pygame.transform.scale(texture_floor, (cell_size, cell_size))
hp_bar = load_image("image/hud/frame.png")
hp_bar = pygame.transform.scale(hp_bar, (275, 20))
door = load_image("image/castledoors.png")
door = pygame.transform.scale(door, (cell_size, cell_size))
frame = load_image("image/hud/button_1(frame).png")
frame = pygame.transform.scale(frame, (cell_size, cell_size))
blood_screen = load_image("image/BloodOverlay.png")
blood_screen = pygame.transform.scale(blood_screen, (WIDTH, HEIGHT))
# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()
equipment_sprites = pygame.sprite.Group()
inventory_sprites = pygame.sprite.Group()
character_sprites = pygame.sprite.Group()


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["ДОБРО ПОЖАЛОВАТЬ В PYDUNGEON",
                  "Для того, чтобы выбраться от сюда,",
                  "Вам понадобится пройти три уровня катакомб и побороть невиданных чудищ",
                  "Если Вы псих, нажмите любую кнопку"]

    fon = pygame.transform.scale(load_image('image/dungeon_intro.jpeg'), (WIDTH, HEIGHT))
    sc.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('yellow'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        sc.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()


def level2_screen():
    intro_text = ["ВЫ СМОГЛИ ПРОЙТИ ПЕРВЫЙ УРОВЕНЬ ПОДЗЕМЕЛЬЯ",
                  "но это еще не конец...",
                  "Впереди Вас ждут еще более сильные противники",
                  "и гораздо меньше шансов на выживание"]

    fon = pygame.transform.scale(load_image('image/level2_dungeon.jpg'), (WIDTH, HEIGHT))
    sc.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('yellow'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        sc.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()


def level3_screen():
    intro_text = ["НЕМНОГИЕ ЗАХОДИЛИ ТАК ДАЛЕКО",
                  "И еще никто не возвращался",
                  "С последнего, самого мрачного и глубокого уровня",
                  "Смельчак ли ты или безумец?"]

    fon = pygame.transform.scale(load_image('image/level3_dungeon.jpg'), (WIDTH, HEIGHT))
    sc.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('yellow'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        sc.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()


def gameover_screen():
    intro_text = ["В следующий раз повезет",
                  "возможно..."]

    fon = pygame.transform.scale(load_image('image/gameover.jpg'), (WIDTH, HEIGHT))
    sc.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 700
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('yellow'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        sc.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()


def victory_screen():
    intro_text = ["Это победа!",
                  "Вы смогли выбраться из подземелья,",
                  "что обеспечит Вам богатство и славу на всю жизнь"]

    fon = pygame.transform.scale(load_image('image/victory.jpg'), (WIDTH, HEIGHT))
    sc.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 700
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('yellow'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        sc.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()

def exit_screen():
    button_exit = Button(575, 500, 45, 30, "Ок")
    name = ''

    fon = pygame.transform.scale(load_image('image\exit.jpg'), (WIDTH, HEIGHT))
    sc.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    
    title = font.render('Напиши свое имя', True, (255, 255, 255))

    while True:
        sc.blit(fon, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    name += event.unicode
                elif event.key == K_BACKSPACE:
                    name = name[:-1]
                elif event.key == K_RETURN:
                    name = ""
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_exit.push_button(event.pos):
                    gameover(name, killed_monsters)
        
        text = font.render(name, True, (255, 255, 255))
        rect = text.get_rect()
        rect.center = (600, 400)
        
        button_exit.draw()
        sc.blit(text, rect)
        sc.blit(title, (500, 250))

        pygame.display.flip()

def exchange_equipment_inventory(inventory, hero):
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

    if obj.get_name() == "Leg_armor1" or obj.get_name() == 'Leg_armor2':
        old_w = hero.replace_leg(obj)
        inventory.board[inventory.selected_cell[0]][inventory.selected_cell[1]] = old_w

    if obj.get_name() == "Arm_armor1" or obj.get_name() == 'Arm_armor2':
        old_w = hero.replace_bracers(obj)
        inventory.board[inventory.selected_cell[0]][inventory.selected_cell[1]] = old_w


    if obj.get_type() == "potion":
        if obj.get_name() == "Small_health":
            if hero.health + 5 <= hero.max_health:
                hero.health += 5
            else:
                hero.health = hero.max_health
        elif obj.get_name() == "Small_strength":
            hero.max_health += 5
        inventory.clear_cell()
    return inventory, hero


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


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    fire = [load_image("image/bloodsplats.png")]
    fire[0] = pygame.transform.scale(fire[0], (int(cell_size * 0.2), int(cell_size * 0.2)))
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy, screen_rect):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()
        self.screen_rect = screen_rect
        # у каждой частицы своя скорость — это вектор
        self.velocity = [0, 0]
        self.velocity[0] = random.randrange(-1, 1)
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = GRAVITY

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(self.screen_rect):
            self.kill()


GRAVITY = 0.5


def create_particles(position, screen_rect):
    # количество создаваемых частиц
    particle_count = 20
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers), screen_rect)

def gameover(name, score):
    con = sqlite3.connect("Data_Base.db")
    cur = con.cursor()

    if name == '':
        name = 'аноним'

    cur.execute(f"""INSERT INTO result_table(name, murders) VALUES('{name}', '{score}')""")

    con.commit()
    con.close()
    terminate()