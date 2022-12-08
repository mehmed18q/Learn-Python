import pygame, sys
from pygame.locals import *

pygame.init()

win = pygame.display.set_mode((800, 600))
points = []
black = (0, 0, 0)
cyan = (0, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                points.append(event.pos)
            if event.button == 3:
                if len(points) >= 1:
                    points.pop()
                # print(points)
        if event.type == MOUSEMOTION:
            if len(points) >= 2:
                points[-1] = event.pos
    win.fill(black)
    if len(points) >= 2:
        pygame.draw.lines(win, cyan, True, points, 2)
    pygame.display.update()