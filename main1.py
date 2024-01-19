import random
from random import choice, sample
import pygame
import sys
import os
import pygame

pygame.mixer.init()
pygame.mixer.music.load('Anna_Asti_-_Carica_76836128.mp3')
pygame.mixer.music.play(999)
pygame.init()
screen = pygame.display.set_mode((500, 500))
img = pygame.image.load('data\судоку.jpg')
pygame.display.set_caption("Aлёна лох объелась блох")
pygame.display.set_icon(img)
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
FPS = 60
GRAVITY = 1
x, y = 0, 0
dif = 500 / 9
val = 0
count = 0
a = 3
side = a * a
width, height = 500, 500
c = 0
maps = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

maps_ans = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
table = [[True, True, True, True, True, True, True, True, True] for _ in range(9)]
level = 0


class Sudoku1:
    def sud(self):
        global maps, c, side, maps_ans, level, table
        c = 0
        while c != 9:
            c = 0
            hor = [set(range(1, 10)) for _ in range(10)]
            ver = [set(range(1, 10)) for _ in range(10)]
            kvadr = [[set(range(1, 10)), set(range(1, 10)), set(range(1, 10))] for _ in range(3)]
            maps = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
            maps_ans = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
            table = [[True, True, True, True, True, True, True, True, True] for _ in range(9)]
            for i in range(9):
                for j in range(9):

                    a = hor[i] & ver[j] & kvadr[i // 3][j // 3]
                    a = list(a)
                    if a:
                        r = random.choice(a)
                        maps[i][j] = r
                        maps_ans[i][j] = r
                        hor[i].remove(r)
                        ver[j].remove(r)
                        kvadr[i // 3][j // 3].remove(r)
            for p in range(len(maps)):
                if maps[p].count(0) == 0:
                    c += 1
        ans = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        for i in range(len(maps_ans)):
            for j in range(len(maps_ans[i])):
                ans[i][j] = maps_ans[j][i]

        # pереворачиваем масив ответов
        print(ans)

        squares = side * side
        empties = squares * level // 4  # УРОВЕНЬ СЛОЖНОСИ 1-3
        for p in sample(range(squares), empties):
            maps[p // side][p % side] = 0
            table[p // side][p % side] = False
            # maps[0][0] = 0
        with open("file.txt", "w") as output:
            for i in ans:
                output.write(str(i))
                output.write('\n')  # КАРТА ПЕРЕВЕРНУТАЯ


font1 = pygame.font.SysFont(None, 50)  # но можно найти прикольный шрифт
font2 = pygame.font.SysFont(None, 20)


def get_level(pos):
    global level
    x = pos[0]
    y = pos[1]
    if x > 15 and x < 150 and y > 380 and y < 425:
        level = 1
        draw()
    elif x > 190 and x < 320 and y > 380 and y < 425:
        level = 2
        draw()
    elif x > 350 and x < 480 and y > 380 and y < 430:
        level = 3
        draw()
    Sudoku1().sud()


# (15, 379)-(148, 425) - 1 level
# (189, 379)-(320, 424)-2 level
# (352, 380)-(479, 427) -3 level
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
            elif event.type == pygame.MOUSEBUTTONDOWN:

                return game_rules()
        pygame.display.flip()
        clock.tick(FPS)


def game_rules():
    intro_text = ["От игрока требуется заполнить свободные клетки",
                  "цифрами от 1 до 9 так, чтобы в каждой строке, ",
                  "в каждом столбце и в каждом малом квадрате 3×3",
                  "каждая цифра встречалась бы только один раз", "",
                  "Выберите уровень и войдите в игру"]

    fon = pygame.transform.scale(load_image('jon.png'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 25)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # x=pos[0]
                # y=pos[1]
                # if (x > 15 and x < 150 and y > 380 and y < 425) or (x > 190 and x < 320 and y > 380 and y < 425) or (x > 350 and x < 480 and y > 380 and y < 430):
                get_level(pos)
                if level:
                    return
        pygame.display.flip()
        clock.tick(FPS)


# ИГРОВОЙ ДВИЖОК#
def get_cord(pos):
    global x
    x = pos[0] // dif
    global y
    y = pos[1] // dif


# ВНЕШНЯЯ ОТРИСОВКА ПОЛЯ
def draw_box():
    global table
    if table[int(x)][int(y)] == False:
        for i in range(2):
            pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
            pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)


#
# sec = 0


# отрисовка клеток и их заполнение
def draw():
    # global sec
    #
    # time.sleep(1)
    # sec += 1
    # print(sec)
    if not level:
        game_rules()
    for i in range(9):
        for j in range(9):
            if maps[i][j] != 0:  # цвет фона
                pygame.draw.rect(screen, (255, 255, 255), (i * dif, j * dif, dif + 1, dif + 1))
                if table[i][j] == True:
                    text1 = font1.render(str(maps[i][j]), 1, (0, 0, 0))  # цвет цифр
                    screen.blit(text1, (i * dif + 15, j * dif + 10))
                else:
                    text1 = font1.render(str(maps[i][j]), 1, (255, 0, 0))  # цвет цифр
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
def draw_val(val, color):
    global table
    print(table)
    if table[int(x)][int(y)] == False:
        text1 = font1.render(str(val), 1, color)
        screen.blit(text1, (x * dif + 15, y * dif + 15))
    else:
        text1 = font1.render(str(val), 1, color)
        screen.blit(text1, (x * dif + 15, y * dif + 15))


# ОБРАБОТКА ОШИБОК(вообще они не нужны, т.к. выводиться текст, а у нас его нет
# понять что это
def raise_error1():
    text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
    screen.blit(text1, (20, 450))


# если в клетке 0
def raise_error2():
    text1 = font2.render(str(val), 1, (255, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)


# проверка подлинности значения
def valid(maps, i, j, val, maps_ans):
    global table
    if table[i][j] == True:
        return
    if val == maps_ans[i][j]:
        maps[i][j] = val
        table[i][j] = True
        return True
    else:
        maps[i][j] = 0
        table[i][j] = False
        # x = i
        # y = j
        # for i in range(2):
        #     pygame.draw.line(screen, (255, 122, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        #     pygame.draw.line(screen, (255, 122, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)

    return False


# for it in range(9):[
#     if m[i][it] == val:
#         return False
#     if m[it][j] == val:
#         return False
# it = i // 3
# jt = j // 3
# for i in range(it * 3, it * 3 + 3):
#     for j in range(jt * 3, jt * 3 + 3):
#         if m[i][j] == val:
#             return False
# return True


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
    global maps, maps_ans, count
    count= 0
    maps = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
        if count == 0 or count == 1:
            create_stars()
            count += 1
        all_sprites.update()
        fon = pygame.transform.scale(load_image('end_screen.png'), ((width, height)))
        screen.blit(fon, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


screen_rect = (0, 0, width, height)


class Feyerverk(pygame.sprite.Sprite):
    fire = [load_image("star.png", -1)]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = 255, 255
        self.gravity = 0.07

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.rect.colliderect(screen_rect) == False:
            self.kill()


def create_stars():
    particle_count = 100
    numbers = range(-10, 10)
    for _ in range(particle_count):
        Feyerverk(random.choice(numbers), random.choice(numbers))
    return x


run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0
is_true = True
if __name__ == '__main__':
    start_screen()
    # a = Sudoku1()
    # a.sud()
    Sudoku1().sud()
    print(maps, maps_ans, sep='\n')
    run = True
    while run:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag1 = 1
                pos = pygame.mouse.get_pos()
                get_cord(pos)
                print(x, y)
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
            if not solve(maps, 0, 0):
                error = 1
            else:
                rs = 1
            flag2 = 0
        if (val != 0) and (table[int(x)][int(y)] == False):
            if maps[int(x)][int(y)] == maps_ans[int(x)][int(y)]:
                color = (0, 0, 0)
            else:
                color = (255, 0, 0)
            draw_val(val, color)
            print(int(x))
            print(int(y))
            print(val, color)

            if valid(maps, int(x), int(y), val, maps_ans):
                table[int(x)][int(y)] = True
                maps[int(x)][int(y)] = val
                flag1 = 0
            else:
                maps[int(x)][int(y)] = val
                is_true = False
                while maps[int(x)][int(y)] != val:
                    flag1 = 1
            val = 0
        else:
            val = 0

        if error == 1:
            raise_error1()

        if not (maps.count([0] * 9)) and maps == maps_ans:
            print(maps == maps_ans)
            final()
            a = Sudoku1()
            a.sud()
            level = 0

        else:
            draw()
        if flag1 == 1:
            draw_box()
        pygame.display.update()

pygame.quit()
