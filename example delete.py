import random
import pygame
import sys
import os

pygame.font.init()

screen = pygame.display.set_mode((500, 500))

img = pygame.image.load('data\судоку.jpg')
pygame.display.set_icon(img)

x = 0
y = 0
dif = 500 / 9
val = 0

# ПОЛЕ

from random import sample

a = 3
side = a * a


def pattern(r, c):
    return (a * (r % a) + r // a + c) % side


def shuffle(s):
    return sample(s, len(s))


rBase = range(a)
rows = [g * a + r for g in shuffle(rBase) for r in shuffle(rBase)]
cols = [g * a + c for g in shuffle(rBase) for c in shuffle(rBase)]
nums = shuffle(range(1, a * a + 1))

maps = [[nums[pattern(r, c)] for c in cols] for r in rows]

maps_ans = maps  # ответы

squares = side * side
empties = squares * 1 // 4  # ОТ 1 ДО 3 УРОВЕНЬ СЛОЖНОСИ
for p in sample(range(squares), empties):
    maps[p // side][p % side] = 0

font1 = pygame.font.SysFont(None, 50)  # но можно найти прикольный шрифт
font2 = pygame.font.SysFont(None, 20)

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
FPS = 50


# КАРТИНКИ НАЧАЛО#
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображениями '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["ДОБРО ПОЖАЛОВАТЬ В МИР СУДОКУ!"]

    fon = pygame.transform.scale(load_image('судоку.jpg'), ((width, height)))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('blue'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return game_rules()
        pygame.display.flip()
        clock.tick(FPS)


def game_rules():
    intro_text = ["От игрока требуется заполнить свободные клетки",
                  "цифрами от 1 до 9 так, чтобы в каждой строке, ",
                  "в каждом столбце и в каждом малом квадрате 3×3",
                  "каждая цифра встречалась бы только один раз", "",
                  "Выберите уровень и войдите в игру"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    draw()


# ИГРОВОЙ ДВИЖОК#
def get_cord(pos):
    global x
    x = pos[0] // dif
    global y
    y = pos[1] // dif


# ВНЕШНЯЯ ОТРИСОВКА ПОЛЯ
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)


# отрисовка клеток и их заполнение
def draw():
    for i in range(9):
        for j in range(9):
            if maps[i][j] != 0:  # цвет фона
                pygame.draw.rect(screen, (255, 255, 255), (i * dif, j * dif, dif + 1, dif + 1))
                text1 = font1.render(str(maps[i][j]), 1, (0, 0, 0))  # цвет цифр
                screen.blit(text1, (i * dif + 15, j * dif + 10))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (i * dif, j * dif, dif + 1, dif + 1))

    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)


# заполнение значения
def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))


# ОБРАБОТКА ОШИБОК(вообще они не нужны, т.к. выводиться текст, а у нас его нет
# понять что это
def raise_error1():
    text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
    screen.blit(text1, (20, 450))


# если в клетке 0
def raise_error2():
    text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
    screen.blit(text1, (20, 470))


# проверка подлинности значения
def valid(m, i, j, val):
    for it in range(9):
        if m[i][it] == val:
            return False
        if m[it][j] == val:
            return False
    it = i // 3
    jt = j // 3
    for i in range(it * 3, it * 3 + 3):
        for j in range(jt * 3, jt * 3 + 3):
            if m[i][j] == val:
                return False
    return True


# заполнение готовых значений(нам это надо?)
def solve(maps, i, j):
    while maps[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()
    for it in range(1, 10):
        if valid(maps, i, j, it) == True:
            maps[i][j] = it
            global x, y
            x = i
            y = j
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(maps, i, j) == 1:
                return True
            else:
                maps[i][j] = 0
            screen.fill((255, 255, 255))

            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)
    return False


# после завершения игры картинкаю добавить кнопку, которая перебрысывает на выбор уровня (заново)
def final():
    fon = pygame.transform.scale(load_image('fon.jpg'), ((width, height)))  # ФИНАЛЬНАЯ КАРТИНКА
    screen.blit(fon, (0, 0))


run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0
if __name__ == '__main__':
    running = True
    start_screen()
    while run:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag1 = 1
                pos = pygame.mouse.get_pos()
                get_cord(pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= 1
                    flag1 = 1
                if event.key == pygame.K_RIGHT:
                    x += 1
                    flag1 = 1
                if event.key == pygame.K_UP:
                    y -= 1
                    flag1 = 1
                if event.key == pygame.K_DOWN:
                    y += 1
                    flag1 = 1
                if event.key == pygame.K_1:
                    val = 1
                if event.key == pygame.K_2:
                    val = 2
                if event.key == pygame.K_3:
                    val = 3
                if event.key == pygame.K_4:
                    val = 4
                if event.key == pygame.K_5:
                    val = 5
                if event.key == pygame.K_6:
                    val = 6
                if event.key == pygame.K_7:
                    val = 7
                if event.key == pygame.K_8:
                    val = 8
                if event.key == pygame.K_9:
                    val = 9
                if event.key == pygame.K_RETURN:
                    flag2 = 1

        if flag2 == 1:
            if solve(maps, 0, 0) == False:
                error = 1
            else:
                rs = 1
            flag2 = 0
        if val != 0:
            draw_val(val)
            print(int(x))
            print(int(y))
            print(val)
            if valid(maps, int(x), int(y), val) == True:
                print('True')
                maps[int(x)][int(y)] = val
                flag1 = 0
            else:
                maps[int(x)][int(y)] = 0
                raise_error2()
            print('False')
            val = 0
        if maps == maps_ans:
            final()
        if error == 1:
            raise_error1()

        draw()
        if flag1 == 1:
            draw_box()
        pygame.display.update()

pygame.quit()
