import pygame, sys
from pygame.locals import *

pygame.init()

height = 600
width = 800
cat_x = 380
cat_y = 300
cat_w = 80
cat_h = 80
speed = 20
cat_s = 10

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")
bg = pygame.image.load("a.jpg")
BG = pygame.transform.scale(bg, (width, height))


while True:
    char = pygame.image.load("cat.png")
    CHAR = pygame.transform.scale(char, (cat_w, cat_h))
    win.blit(BG, (0, 0))
    win.blit(CHAR, (cat_x, cat_y))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1: # left click
                cat_x -= speed
            if event.button == 2: # scrol click
                cat_w = 80
                cat_h = 80
                cat_x = 260
                cat_y = 410
            if event.button == 3: # right click
                cat_x += speed
            if event.button == 4: # scrol up
                cat_w += cat_s
                cat_h += cat_s
            if event.button == 5: # scrol down
                cat_w -= cat_s
                cat_h -= cat_s
                if cat_w < 0 or cat_h < 0:
                    cat_w = 80
                    cat_h = 80
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                cat_y += speed
            if event.key == K_UP:
                cat_y -= speed
    pygame.display.update()