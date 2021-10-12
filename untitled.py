import pygame
import pygame.freetype
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))

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
    Рисует шарик
    """
    global x, y, r, color, Vx, Vy
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    Vx = randint(-20, 20)
    Vy = randint(-20, 20)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    

def click(event):
    print(x, y, r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
global score, killed
score = 0
f1 = pygame.freetype.Font(None, 36)
killed = 0

new_ball()
while not finished:
    clock.tick(FPS)
    if killed == 1:
        new_ball()
        killed = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x1 = event.pos[0]
            y1 = event.pos[1]
            if (x1-x)**2+(y1-y)**2-r**2 <= 0:
                score+=1
                killed = 1
    if killed == 1:
        continue
    text1 = f1.render_to(screen, (600, 36), f"{score}", (180, 0, 0))
    x+=Vx
    y+=Vy
    if x >= 1200-r:
        Vx = -Vx
        circle(screen, color, (1200-r, y), r)
    elif x <= r:
        Vx = -Vx
        circle(screen, color, (r, y), r)
    elif y >= 900-r:
        Vy = -Vy
        circle(screen, color, (x, 900-r), r)
    elif y <= r:
        Vy = -Vy
        circle(screen, color, (x, r), r)
    else:
        circle(screen, color, (x, y), r)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
