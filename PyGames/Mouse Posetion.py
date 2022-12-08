import pygame, sys
from pygame.locals import *


win = pygame.display.set_mode((800, 600))
x = 0
y = 0
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
purple = (150, 0, 150)
yellow = (255, 255, 0)
color = red

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            x, y = event.pos
        win.fill(black)
        pygame.draw.line(win, color, (x, 0), (x, 600), 5)
        pygame.draw.line(win, color, (0, y), (800, y), 5)
        if event.type == KEYDOWN:
            if event.key == K_r:
                color = red
            if event.key == K_g:
                color = green
            if event.key == K_p:
                color = purple
            if event.key == K_c:
                color = cyan
            if event.key == K_y:
                color = yellow
            if event.key == K_SPACE:
                print(f'({color}, {x}, {y})')

        pygame.display.update()
