import pygame, sys
from pygame.locals import *

pygame.init()

win = pygame.display.set_mode((800, 600))
points = []
points2 = []
black = (0, 0, 0)
cyan = (0, 255, 255)
yellow = (255, 255, 0)
draw = False
first_draw = False
second_draw = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_1:
                first_draw = True
                second_draw = False
            if event.key == K_2:
                first_draw = False
                second_draw = True
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and first_draw:
                points.append(event.pos)
                draw = True
            if event.button == 1 and second_draw:
                points2.append(event.pos)
            if event.button == 3:
                if len(points) >= 1:
                    points.pop()
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                draw = False
        if event.type == MOUSEMOTION and draw:
            if len(points) >= 2:
                points[-1] = event.pos
    win.fill(black)
    if len(points) >= 2:
        pygame.draw.lines(win, cyan, False, points, 2)
    if len(points2) >= 2:
        pygame.draw.lines(win, yellow, False, points2, 2)
    pygame.display.update()