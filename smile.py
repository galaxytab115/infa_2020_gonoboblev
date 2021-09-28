import numpy as np
import pygame
from pygame.draw import *

pygame.init()

white = (255, 255, 255)
FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill(white)

circle(screen, (200, 179, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 1)

circle(screen, (255, 0, 0), (150, 160), 18)
circle(screen, (0, 0, 0), (150, 160), 18, 1)
circle(screen, (0, 0, 0), (150, 160), 8)
circle(screen, (255, 0, 0), (240, 160), 14)
circle(screen, (0, 0, 0), (240, 160), 14, 1)
circle(screen, (0, 0, 0), (240, 160), 8)

polygon(screen, (0, 0, 0), [(100, 120), (190, 150)], 10)
polygon(screen, (0, 0, 0), [(300, 120), (200, 160)], 10)
polygon(screen, (0, 0, 0), [(150, 250), (250, 250)], 30)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
