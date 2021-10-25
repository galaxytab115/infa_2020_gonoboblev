import pygame.freetype
from pygame.draw import *
from random import randint

"""
Игра "Поймай шарик"
Программа считывает имя игрока, после чего открывается окно игры. На игровом поле создается
от 3 до 10 шариков в рандомных местах с рандомным радиусом и скоростью, и от 3 до 7 квадратиков
в рандомных местах с рандомной стороной и скоростью. Задача кликнуть по шарику или квадратику.
При попадании по шарику дается 1 очко, при попадании по квадратику дается 1, 2, 3 и так далее 
очков, но квадратики ускоряются с каждым убитым. Если шарик ударяется 11 раз об стенку, он пропадает,
если квадратик ударяется об стенку 6 раз, он пропадает. Игра заканчивается, когда все шарики и  
квадратики пропадут. Выйти из игры можно, нажав на клавишу ESCAPE. Счет игрока с его именем заносятся
в файл score.txt, в той же директории, что и файл игры. Если такого файла нет, он автоматически создается.
"""

#Считывание имени игрока
print("Введите ваше имя: ")
name = str(input())
pygame.init()

FPS = 90
screen = pygame.display.set_mode((1200, 600))

#COLORS
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    """
    Функция рассчитывает случайные координаты шарика, радиус, скорости по осям и цвет
    :return: возвращает список вышеперечисленных значений
    """
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    Vx = randint(-20, 20)
    Vy = randint(-20, 20)
    color = COLORS[randint(0, 5)]
    return [x, y, r, Vx, Vy, color, 0, 0]

def new_kube(V):
    """
    Функция рассчитывает случайные координаты квадратика, длину стороны, скорости по осям и цвет
    :param V: множитель скорости
    :return: возвращает список вышеперечисленных значений
    """
    x = randint(100, 700)
    y = randint(100, 500)
    a = randint(40, 60)
    Vx = randint(-15, 15)
    Vy = randint(-15, 15)
    color = COLORS[randint(0, 5)]
    return [x, y, a, Vx+3*V, Vy+3*V, color, 0, 0]


pygame.display.update()
clock = pygame.time.Clock()
score = 0
finished = False
f1 = pygame.freetype.Font(None, 36)

#Рассчет количества шариков и квадратиков
V = 1
n = randint(3, 8)
m = randint(3, 11)
A = [new_ball() for i in range(1, m)]
B = [new_kube(1) for k in range(1, n)]

#Начальная отрисовка фигур
for el in A:
    circle(screen, el[5], (el[0], el[1]), el[2])
for el in B:
    rect(screen, el[5], (el[0]-el[2], el[1]-el[2], 2*el[2], 2*el[2]))

#Основной цикл
while not finished:
    clock.tick(FPS)
    x1 = 0
    y1 = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Считывание координат мыши
            x1 = event.pos[0]
            y1 = event.pos[1]
        elif event.type == pygame.KEYDOWN:
            #Выход по кнопке ESCAPE
            if event.key == pygame.K_ESCAPE:
                finished = True
    for el in A:
        #Проверка попадания по шарику и подсчет очков
        if (el[0]-x1)**2+(el[1]-y1)**2 <= el[2]**2:
            el[6] = 1
            score += 1
        if el[7] >= 11:
            el[6] = 1
        el[0] += el[3]
        el[1] += el[4]
        #Отрисовка нового шарика и подсчет количества ударов об стенку
        if el[6] == 0:
            if el[0] >= 1200 - el[2]:
                el[3] = (-1)*el[3]
                el[7] += 1
                circle(screen, el[5], (1200 - el[2], el[1]), el[2])
            elif el[0] <= el[2]:
                el[3] = (-1)*el[3]
                el[7] += 1
                circle(screen, el[5], (el[2], el[1]), el[2])
            if el[1] >= 600 - el[2]:
                el[4] = (-1)*el[4]
                el[7] += 1
                circle(screen, el[5], (el[0], 600 - el[2]), el[2])
            elif el[1] <= el[2]:
                el[4] = (-1)*el[4]
                el[7] += 1
                circle(screen, el[5], (el[0], el[2]), el[2])
            else:
                circle(screen, el[5], (el[0], el[1]), el[2])
    #Создание нового шарика при убийстве существующего, при условии, что шарик ударился об стенку не более 10 раз
    for i in range(0, m-1):
        if A[i][6] == 1 and A[i][7] < 11:
            A[i] = new_ball()
    for el in B:
        #Проверка попадания по квадратику и подсчет очков
        if (el[0]-x1)**2+(el[1]-y1)**2 <= el[2]**2:
            el[6] = 1
            score += V
            V += 1
        if el[7] >= 6:
            el[6] = 1
        el[0] += el[3]
        el[1] += el[4]
        #Отрисовка квадратика и подсчет количества ударов об стенку
        if el[6] == 0:
            if el[0] >= 1200 - el[2]:
                el[3] = (-1)*el[3]
                el[7] += 1
                rect(screen, el[5], (1200 - 2*el[2], el[1]-el[2], 2*el[2], 2*el[2]))
            elif el[0] <= el[2]:
                el[3] = (-1)*el[3]
                el[7] += 1
                rect(screen, el[5], (0, el[1]-el[2], 2*el[2], 2*el[2]))
            if el[1] >= 600 - el[2]:
                el[4] = (-1)*el[4]
                el[7] += 1
                rect(screen, el[5], (el[0]-el[2], 600 - 2*el[2], 2*el[2], 2*el[2]))
            elif el[1] <= el[2]:
                el[4] = (-1)*el[4]
                el[7] += 1
                rect(screen, el[5], (el[0]-el[2], 0, 2*el[2], 2*el[2]))
            else:
                rect(screen, el[5], (el[0]-el[2], el[1]-el[2], 2*el[2], 2*el[2]))
    #Создание нового квадратика при убийстве существующего, при условии, что квадратик ударился об стенку не более 5 раз
    for i in range(0, n-1):
        if B[i][6] == 1 and B[i][7] < 6:
            B[i] = new_kube(V)
    #Вывод счета
    text1 = f1.render_to(screen, (600, 36), f"{score}", (180, 0, 0))
    pygame.display.update()
    screen.fill(BLACK)
#Запись в файл имени и счета игрока
f = open('score.txt', 'a')
f.write('Игрок ' + name + ' набрал ' + str(score) + ' очков \n')
f.close()
pygame.quit()