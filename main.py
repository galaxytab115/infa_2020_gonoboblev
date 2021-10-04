import pygame
import numpy as np
pygame.init()

# константы \/
FPS = 30
screen_size = (500, 700)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
GREEN = (24, 99, 24)
GREY = (100, 100, 100)
PINK = (255, 192, 203)
GREY_FOR_KLUBOK = (204, 204, 204)
POL = (147, 118, 11)
STENA = (74, 55, 13)
RAMA_OKON = (204, 204, 255)
OKNA = (128, 218, 235)
RIZHI = (215, 125, 49)

# основной экран \/
screen = pygame.display.set_mode(screen_size)
screen.fill((205, 173, 0))

# функция рисует повернутый эллипс a, b - большая и маленькая оси; x, y - корды центра; color - цвет; angle - угол поворота
def coolellipse(color, angle, a, b, x, y):
    surface = pygame.Surface((a, a)).convert_alpha()
    surface.fill([0, 0, 0, 0])
    pygame.draw.ellipse(surface, color, (0, (a-b)/2, a, b))
    pygame.draw.ellipse(surface, (0, 0, 0), (0, (a - b) / 2, a, b), 1)
    surface = pygame.transform.rotate(surface, angle)
    dx = x-a*(abs(np.sin(np.deg2rad(angle)))+abs(np.cos(np.deg2rad(angle))))/2
    dy = y-a*(abs(np.sin(np.deg2rad(angle)))+abs(np.cos(np.deg2rad(angle))))/2
    screen.blit(surface, (dx, dy))
# функция рисует не такой крутой эллипс как выше: эллипс без обводки
def notsocoolellipse(color, angle, a, b, x, y):
    surface = pygame.Surface((a, a)).convert_alpha()
    surface.fill([0, 0, 0, 0])
    pygame.draw.ellipse(surface, color, (0, (a-b)/2, a, b))
    surface = pygame.transform.rotate(surface, angle)
    dx = x-a*(abs(np.sin(np.deg2rad(angle)))+abs(np.cos(np.deg2rad(angle))))/2
    dy = y-a*(abs(np.sin(np.deg2rad(angle)))+abs(np.cos(np.deg2rad(angle))))/2
    screen.blit(surface, (dx, dy))
# времени час ночи мои сосеи легли спать, а только закончил этот эллипс ******

# функция рисует кота: color_body - цвет тела; color_eyes - цвет глвз; size - размер(общий); eyes - направление взгляда
# (вправо 1, влево 2); body - направление самого кота(вправо 1, влево 2); x, y - корды середины туловища кота
def cat(color_body, color_eyes, size, eyes, body, x, y):
    if body == 1:
        coolellipse(color_body, 30, 28*size/40, 9*size/40, x-27*size/40, y+3*size/40)  #хвост
        coolellipse(color_body, 0, size, size/2, x, y)   #тело
        coolellipse(color_body, 90, 9*size/40, 5*size/40, x+20*size/40, y+3*size/40)  #лапа передняя за мордой
        coolellipse(color_body, 0, 2*size/5, 7*size/20, x+17*size/40, y-size/25)  #морда
        coolellipse(color_body, 0, 12*size/40, 12*size/40, x-15*size/40, y+6*size/40)  #бедро
        coolellipse(color_body, 90, size/4, size/10, x-size/2, y+13*size/40)  #лапа задняя
        coolellipse(color_body, 5, 9*size/40, 5*size/40, x+12*size/40, y+7.3*size/40)  #лапа передняя на переднем плане
        coolellipse(color_eyes, 90, 4.5*size/40, 4*size/40, x+13.5*size/40, y-size/25)  #левый глаз
        coolellipse(color_eyes, 90, 4.5*size/40, 4*size/40, x+20.5*size/40, y-size/25)  #правый глаз
        if eyes == 1:
            notsocoolellipse(BLACK, 90, 4*size/40, size/60, x+14*size/40, y-size/25)  #черная штука левого глаза
            notsocoolellipse(BLACK, 90, 4*size/40, size/60, x+21*size/40, y-size/25)  #черная штука правого глаза
            notsocoolellipse(WHITE, 120, 2.25*size/40, 0.6*size/40, x+13.3*size/40, y-1.6*size/25)  #белая штука левого
            notsocoolellipse(WHITE, 120, 2.25*size/40, 0.6*size/40, x+20.3*size/40, y-1.6*size/25)  #белая штука правого
        else:
            notsocoolellipse(BLACK, 90, 4*size/40, size/60, x+13*size/40, y-size/25)  # черная штука левого глаза
            notsocoolellipse(BLACK, 90, 4*size/40, size/60, x+20*size/40, y-size/25)  # черная штука правого глаза
            notsocoolellipse(WHITE, 60, 2.2*size/40, 0.6*size/40, x+13.8*size/40, y-1.6*size/25)  # белая штука левого
            notsocoolellipse(WHITE, 60, 2.2*size/40, 0.6*size/40, x+20.8*size/40, y-1.6*size/25)  # белая штука правого
        pygame.draw.polygon(screen, GREY, [(x+13*size/40, y-size/25-5*size/40), (x+9.5*size/40, y-size/25-8*size/40),
                                            (x+10.5*size/40, y-size/25-2.5*size/40)])
        pygame.draw.polygon(screen, BLACK, [(x+13*size/40, y-size/25-5*size/40), (x+9.5*size/40, y-size/25-8*size/40),
                                            (x+10.5*size/40, y-size/25-2.5*size/40)], 1)
        pygame.draw.polygon(screen, PINK, [(x+12.6*size/40, y-size/25-5*size/40),
                                            (x+9.9*size/40, y-size/25-7.4*size/40),
                                            (x+10.9*size/40, y-size/25-3.1*size/40)])  #ухо левое
        pygame.draw.polygon(screen, GREY, [(x+21*size/40, y-size/25-5*size/40), (x+24.5*size/40, y-size/25-8*size/40),
                                            (x+23.5*size/40, y-size/25-2.5*size/40)])
        pygame.draw.polygon(screen, BLACK, [(x+21*size/40, y-size/25-5*size/40), (x+24.5*size/40, y-size/25-8*size/40),
                                            (x+23.5*size/40, y-size/25-2.5*size/40)], 1)
        pygame.draw.polygon(screen, PINK, [(x+21.4*size/40, y-size/25-5*size/40),
                                            (x+24.1*size/40, y-size/25-7.4*size/40),
                                            (x+23.1*size/40, y-size/25-3.1*size/40)])  # ухо правое
        pygame.draw.polygon(screen, PINK, [(x+17*size/40, y-size/25+3*size/40),
                                            (x+17.5*size/40, y-size/25+2.5*size/40),
                                            (x+16.5*size/40, y-size/25+2.5*size/40)])
        pygame.draw.polygon(screen, BLACK, [(x+17*size/40, y-size/25+3*size/40),
                                            (x+17.5*size/40, y-size/25+2.5*size/40),
                                            (x+16.5*size/40, y-size/25+2.5*size/40)], 1)  #нос
        pygame.draw.line(screen, BLACK, (x+17*size/40, y-size/25+3*size/40),
                                            (x+17*size/40, y-size/25+3*size/40+size/40), 2)
        pygame.draw.arc(screen, BLACK, (x+17*size/40, y-size/25+3*size/40+size/80, size/20, size/20),
                                            0.9*np.pi, 7*np.pi/4, 1)
        pygame.draw.arc(screen, BLACK, (x+17*size/40-0.9*size/20, y-size/25+3*size/40+size/80, size/20, size/20),
                                            5*np.pi/4, 2.1*np.pi, 1)  #ротэльник
        pygame.draw.line(screen, BLACK, (x+19*size/40, y-size/25+4*size/40), (x+29*size/40, y-size/25+2*size/40), 1)
        pygame.draw.line(screen, BLACK, (x+19.5*size/40, y-size/25+4.5*size/40), (x+30*size/40, y-size/25+3*size/40), 1)
        pygame.draw.line(screen, BLACK, (x+19*size/40, y-size/25+5*size/40), (x+29*size/40, y-size/25+4*size/40), 1)
        pygame.draw.line(screen, BLACK, (x + 15 * size / 40, y - size / 25 + 4 * size / 40),
                         (x + 5 * size / 40, y - size / 25 + 2 * size / 40), 1)
        pygame.draw.line(screen, BLACK, (x + 14.5 * size / 40, y - size / 25 + 4.5 * size / 40),
                         (x + 4.5 * size / 40, y - size / 25 + 3 * size / 40), 1)
        pygame.draw.line(screen, BLACK, (x + 15 * size / 40, y - size / 25 + 5 * size / 40),
                         (x + 5 * size / 40, y - size / 25 + 4 * size / 40), 1)
    else:
        coolellipse(color_body, -30, 28 * size / 40, 9 * size / 40, x + 27 * size / 40, y + 3 * size / 40)  # хвост
        coolellipse(color_body, 0, size, size / 2, x, y)  # тело
        coolellipse(color_body, 90, 9 * size / 40, 5 * size / 40, x - 20 * size / 40,
                    y + 3 * size / 40)  # лапа передняя за мордой
        coolellipse(color_body, 0, 2 * size / 5, 7 * size / 20, x - 17 * size / 40, y - size / 25)  # морда
        coolellipse(color_body, 0, 12 * size / 40, 12 * size / 40, x + 15 * size / 40, y + 6 * size / 40)  # бедро
        coolellipse(color_body, 90, size / 4, size / 10, x + size / 2, y + 13 * size / 40)  # лапа задняя
        coolellipse(color_body, -5, 9 * size / 40, 5 * size / 40, x - 12 * size / 40,
                    y + 7.3 * size / 40)  # лапа передняя на переднем плане
        coolellipse(color_eyes, 90, 4.5 * size / 40, 4 * size / 40, x - 13.5 * size / 40, y - size / 25)  # правый глаз
        coolellipse(color_eyes, 90, 4.5 * size / 40, 4 * size / 40, x - 20.5 * size / 40, y - size / 25)  # левый глаз
        if eyes == 2:
            notsocoolellipse(BLACK, 90, 4 * size / 40, size / 60, x - 14 * size / 40,
                             y - size / 25)  # черная штука правого глаза
            notsocoolellipse(BLACK, 90, 4 * size / 40, size / 60, x - 21 * size / 40,
                             y - size / 25)  # черная штука левого глаза
            notsocoolellipse(WHITE, 60, 2.25 * size / 40, 0.6 * size / 40, x - 13.3 * size / 40,
                             y - 1.6 * size / 25)  # белая штука правого
            notsocoolellipse(WHITE, 60, 2.25 * size / 40, 0.6 * size / 40, x - 20.3 * size / 40,
                             y - 1.6 * size / 25)  # белая штука левого
        else:
            notsocoolellipse(BLACK, 90, 4 * size / 40, size / 60, x - 13 * size / 40,
                             y - size / 25)  # черная штука правого глаза
            notsocoolellipse(BLACK, 90, 4 * size / 40, size / 60, x - 20 * size / 40,
                             y - size / 25)  # черная штука левого глаза
            notsocoolellipse(WHITE, 120, 2.2 * size / 40, 0.6 * size / 40, x - 13.8 * size / 40,
                             y - 1.6 * size / 25)  # белая штука правого
            notsocoolellipse(WHITE, 120, 2.2 * size / 40, 0.6 * size / 40, x - 20.7 * size / 40,
                             y - 1.6 * size / 25)  # белая штука левого
        pygame.draw.polygon(screen, GREY, [(x - 13 * size / 40, y - size / 25 - 5 * size / 40),
                                           (x - 9.5 * size / 40, y - size / 25 - 8 * size / 40),
                                           (x - 10.5 * size / 40, y - size / 25 - 2.5 * size / 40)])
        pygame.draw.polygon(screen, BLACK, [(x - 13 * size / 40, y - size / 25 - 5 * size / 40),
                                            (x - 9.5 * size / 40, y - size / 25 - 8 * size / 40),
                                            (x - 10.5 * size / 40, y - size / 25 - 2.5 * size / 40)], 1)
        pygame.draw.polygon(screen, PINK, [(x - 12.6 * size / 40, y - size / 25 - 5 * size / 40),
                                           (x - 9.9 * size / 40, y - size / 25 - 7.4 * size / 40),
                                           (x - 10.9 * size / 40, y - size / 25 - 3.1 * size / 40)])  # ухо левое
        pygame.draw.polygon(screen, GREY, [(x - 21 * size / 40, y - size / 25 - 5 * size / 40),
                                           (x - 24.5 * size / 40, y - size / 25 - 8 * size / 40),
                                           (x - 23.5 * size / 40, y - size / 25 - 2.5 * size / 40)])
        pygame.draw.polygon(screen, BLACK, [(x - 21 * size / 40, y - size / 25 - 5 * size / 40),
                                            (x - 24.5 * size / 40, y - size / 25 - 8 * size / 40),
                                            (x - 23.5 * size / 40, y - size / 25 - 2.5 * size / 40)], 1)
        pygame.draw.polygon(screen, PINK, [(x - 21.4 * size / 40, y - size / 25 - 5 * size / 40),
                                           (x - 24.1 * size / 40, y - size / 25 - 7.4 * size / 40),
                                           (x - 23.1 * size / 40, y - size / 25 - 3.1 * size / 40)])  # ухо правое
        pygame.draw.polygon(screen, PINK, [(x - 17 * size / 40, y - size / 25 + 3 * size / 40),
                                           (x - 17.5 * size / 40, y - size / 25 + 2.5 * size / 40),
                                           (x - 16.5 * size / 40, y - size / 25 + 2.5 * size / 40)])
        pygame.draw.polygon(screen, BLACK, [(x - 17 * size / 40, y - size / 25 + 3 * size / 40),
                                            (x - 17.5 * size / 40, y - size / 25 + 2.5 * size / 40),
                                            (x - 16.5 * size / 40, y - size / 25 + 2.5 * size / 40)], 1)  # нос
        pygame.draw.line(screen, BLACK, (x - 17 * size / 40, y - size / 25 + 3 * size / 40),
                         (x - 17 * size / 40, y - size / 25 + 3 * size / 40 + size / 40), 2)
        pygame.draw.arc(screen, BLACK,
                        (x - 17 * size / 40, y - size / 25 + 3 * size / 40 + size / 80, size / 20, size / 20),
                        0.9 * np.pi, 7 * np.pi / 4, 1)
        pygame.draw.arc(screen, BLACK, (x - 17 * size / 40 - 0.9 * size / 20, y - size / 25 + 3 * size / 40 + size / 80,
                        size / 20, size / 20), 5 * np.pi / 4, 2.1 * np.pi, 1)
        pygame.draw.line(screen, BLACK, (x - 19 * size / 40, y - size / 25 + 4 * size / 40),
                         (x - 29 * size / 40, y - size / 25 + 2 * size / 40), 1)
        pygame.draw.line(screen, BLACK, (x - 19.5 * size / 40, y - size / 25 + 4.5 * size / 40),
                         (x - 30 * size / 40, y - size / 25 + 3 * size / 40), 1)
        pygame.draw.line(screen, BLACK, (x - 19 * size / 40, y - size / 25 + 5 * size / 40),
                         (x - 29 * size / 40, y - size / 25 + 4 * size / 40), 1)
        pygame.draw.line(screen, BLACK, (x - 15 * size / 40, y - size / 25 + 4 * size / 40),
                         (x - 5 * size / 40, y - size / 25 + 2 * size / 40), 1)
        pygame.draw.line(screen, BLACK, (x - 14.5 * size / 40, y - size / 25 + 4.5 * size / 40),
                         (x - 4.5 * size / 40, y - size / 25 + 3 * size / 40), 1)
        pygame.draw.line(screen, BLACK, (x - 15 * size / 40, y - size / 25 + 5 * size / 40),
                         (x - 5 * size / 40, y - size / 25 + 4 * size / 40), 1)
#я так задолбался, я сегодня целый день пишу эту долбанную функцию для рисования кота, а мне еще матан учить...

# функция рисует клубок: fasing 1 вправо ниточка, -1 влево; radius - радиус клубка; x, y - координаты центра клубка
def klubok(fasing, radius, x, y):
    coolellipse(GREY_FOR_KLUBOK, 0, 2*radius, 2*radius, x, y)
    if fasing == 1:
        for i in range(x+radius, x+3*radius):
            pygame.draw.polygon(screen, GREY_FOR_KLUBOK, [(i, radius*np.sin(5*(i-x)/radius)/5+y),
                                                        (i+1, radius*np.sin(5*(i+1-x)/radius)/5+y),
                                                        (i, radius*np.sin(5*(i-x)/radius)/5+y)], 2)
        pygame.draw.arc(screen, BLACK, (x-14*radius/5, y-4*radius/5, 16*radius/5, 16*radius/5), 0, np.pi/3)
        pygame.draw.arc(screen, BLACK, (x-15*radius/5, y-5*radius/5, 18*radius/5, 18*radius/5),
                        np.arcsin(1/9), np.arcsin(7/9))
        pygame.draw.arc(screen, BLACK, (x-17*radius/5, y-7*radius/5, 22*radius/5, 22*radius/5),
                        np.arcsin(4/9), np.arcsin(7/11))
        pygame.draw.arc(screen, BLACK, (x-3*radius/5, y-3*radius/5, 16*radius/5, 16*radius/5),
                        np.pi-np.arcsin(6/8), np.pi-np.arcsin(1/4))
        pygame.draw.arc(screen, BLACK, (x-radius/5, y-radius/5, 12*radius/5, 12*radius/5),
                        np.pi-np.arcsin(2/3), np.pi-np.arcsin(1/6))
        pygame.draw.arc(screen, BLACK, (x, y, 10*radius/5, 10*radius/5),
                        np.pi-np.arcsin(3/5), np.pi-np.arcsin(1/5))
    else:
        for i in range(x-3*radius, x-radius):
            pygame.draw.polygon(screen, GREY_FOR_KLUBOK, [(i, radius*np.sin(5*(i-x)/radius)/5+y),
                                                        (i+1, radius*np.sin(5*(i+1-x)/radius)/5+y),
                                                        (i, radius*np.sin(5*(i-x)/radius)/5+y)], 2)
        pygame.draw.arc(screen, BLACK, (x-2*radius/5, y-4*radius/5, 16*radius/5, 16*radius/5), 2*np.pi/3, np.pi)
        pygame.draw.arc(screen, BLACK, (x-3*radius/5, y-5*radius/5, 18*radius/5, 18*radius/5),
                        np.pi-np.arcsin(7/9), np.pi-np.arcsin(1/9))
        pygame.draw.arc(screen, BLACK, (x-5*radius/5, y-7*radius/5, 22*radius/5, 22*radius/5),
                        np.pi-np.arcsin(7/11), np.pi-np.arcsin(4/11))
        pygame.draw.arc(screen, BLACK, (x-13*radius/5, y-3*radius/5, 16*radius/5, 16*radius/5),
                        np.arcsin(1/4), np.arcsin(6/8))
        pygame.draw.arc(screen, BLACK, (x-11*radius/5, y-radius/5, 12*radius/5, 12*radius/5),
                        np.arcsin(1/6), np.arcsin(2/3))
        pygame.draw.arc(screen, BLACK, (x-10*radius/5, y, 10*radius/5, 10*radius/5),
                        np.arcsin(1/5), np.arcsin(3/5))

pygame.draw.rect(screen, STENA, (0, 0, 500, 312))  #стена
pygame.draw.rect(screen, RAMA_OKON, (0, 37, 62, 200))
pygame.draw.rect(screen, OKNA, (0, 43, 50, 50))
pygame.draw.rect(screen, OKNA, (0, 105, 50, 112))
pygame.draw.rect(screen, RAMA_OKON, (112, 37, 150, 200))
pygame.draw.rect(screen, RAMA_OKON, (325, 37, 150, 200))
pygame.draw.rect(screen, OKNA, (120, 43, 62, 50))
pygame.draw.rect(screen, OKNA, (195, 43, 62, 50))
pygame.draw.rect(screen, OKNA, (333, 43, 62, 50))
pygame.draw.rect(screen, OKNA, (408, 43, 62, 50))
pygame.draw.rect(screen, OKNA, (120, 105, 62, 112))
pygame.draw.rect(screen, OKNA, (195, 105, 62, 112))
pygame.draw.rect(screen, OKNA, (333, 105, 62, 112))
pygame.draw.rect(screen, OKNA, (408, 105, 62, 112))  #окна
#урааа осталось только накидать котов и клубков, как это уже надоело
cat(RIZHI, GREEN, 150, 1, 2, 337, 375)
cat(GREY, CYAN, 150, 1, 1, 150, 475)
klubok(2, 19, 155, 362) #мал нитка влево
klubok(2, 19, 112, 582) #мал нитка влево
klubok(2, 19, 362, 662) #мал нитка влево
klubok(1, 19, 407, 482) #мал нитка вправо
klubok(1, 38, 325, 525) #ср нитка вправо
klubok(1, 38, 425, 607) #ср нитка вправо
klubok(2, 56, 225, 620) #большой нитка влево
cat(RIZHI, GREEN, 50, 2, 1, 92, 375)
cat(RIZHI, GREEN, 50, 2, 1, 455, 507)
cat(RIZHI, GREEN, 50, 1, 2, 337, 595)
cat(GREY, CYAN, 50, 1, 1, 100, 662)
cat(GREY, CYAN, 50, 2, 2, 437, 660)
# Я ЗАКОНЧИЛ !!!!!!!!!!! УРААААААААААААА !!!!!!!!!!!!!!!!!!!! АААААААААААААААААААААААААААААААААААААААААААААААААААААААА
# АААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААА
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()