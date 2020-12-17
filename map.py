from settings import *
import random

# 1 - стена
# 2 - проход
# 3 - выход - еще не сделано

# text_map = [
#     '111111111111',
#     '100000001001',
#     '100010010101',
#     '100011110001',
#     '101000000101',
#     '100001100001',
#     '111111111111'
# ]

map_width = 13
map_height = 13


# мой алгоритм генерации лабиринта (куча костылей и не факт что работает)
def map_generation(map_width, map_height):
    map = []
    for i in range(0, map_width):
        for j in range(0, map_height):
            if i == 0 and j == 0:
                map[i][j] = 0
            elif i % 2 != 0 and j % 2 != 0:
                map[i][j] = 1
            else:
                map[i][j] = 0
    entrance = random.randint(1, map_width // 2)
    entrance = 3  # TODO: сделать рандомную генерацию входа
    col = 1
    row = entrance
    map[row][col] = 2

    # вывод на консоль
    for i in range(0, map_width):
        for j in range(0, map_height):
            print(map[i][j])
        print()
    print()
    while col < map_width - 1 and row < map_height - 1:
        x = 0
        y = 0
        # выбираем направление движения
        while True:
            x = random.randint(-1, 1)
            if not x:
                y = random.randint(-1, 1)
                if not x:
                    break
            else:
                break
        # проверяем за границей массива
        if col + x * 2 == map_width or row + y * 2 == map_height:
            map[row + y][col + x] = 3
            break
        elif col + x * 2 > map_width - 1 or row + y * 2 > map_height - 1 \
                or col + x * 2 <= 0 or row + y * 2 <= 0:
            continue

        # делаем проход между клетками
        if map[row + (2 * y)][col + (2 * x)] == 1:
            map[row + y][col + x] = 2
            map[row + 2 * y][col + 2 * x] = 2
            col += 2 * x
            row += 2 * y
        clear = False
        while not clear:
            for i in range(1, map_width - 1, 2):
                for j in range(1, map_height - 1, 2):
                    if map[i][j] == 2:
                        deadend = False
                        ii = i
                        jj = j
                        while not deadend:
                            x = 0
                            y = 0
                            while True:
                                x = random.randint(-1, 1)
                                if not x:
                                    y = random.randint(-1, 1)
                                    if not x:
                                        break
                                else:
                                    break
                            if j + x * 2 >= map_width - 1 or i + y * 2 >= map_height \
                                    or j + x * 2 <= 0 or i + y * 2 <= 0:
                                continue
                            elif map[i + x * 2] != 1 or map[i + y * 2] != 1:
                                deadend = True
                            if map[ii + 2 * y][jj + 2 * x] == 1:
                                map[ii + y][jj + x] = 2
                                map[ii + 2 * y][jj + 2 * x] = 2
                                ii += 2 * x
                                jj += 2 * y

                            clear = True
                            if 1 in map:
                                clear = False

                            for i in range(0, map_width):
                                for j in range(0, map_height):
                                    print(map[i][j])
                                print()
                            print()


text_map = map_generation(map_width, map_height)
# размеры карты (в клеточках)

world_map = set()
# row - координата x (строка, итерация по столбцам)
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == '1':
            world_map.add((i * TILE, j * TILE))
