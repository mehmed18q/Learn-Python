import pygame, sys, random
from pygame.locals import *

pygame.init()

# variables

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
gray = (30, 30, 30)
fps = 30
win_width = 800
win_height = 600
worm_x = 380
worm_y = 280
speed_worm_x = 0
speed_worm_y = 0
food_x = random.randrange(0, 780, 20)
food_y = random.randrange(0, 580, 20)


win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("SnakeGame")
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                speed_worm_x = 20
                speed_worm_y = 0
            if event.key == K_LEFT:
                speed_worm_x = -20
                speed_worm_y = 0
            if event.key == K_DOWN:
                speed_worm_y = 20
                speed_worm_x = 0
            if event.key == K_UP:
                speed_worm_y = -20
                speed_worm_x = 0
    win.fill(black)
    worm_x += speed_worm_x
    worm_y += speed_worm_y
    if worm_x < 0:
        worm_x = 800
    if worm_x > 800:
        worm_x = 0
    if worm_y < 0:
        worm_y = 600
    if worm_y > 600:
        worm_y = 0
    pygame.draw.rect(win, green, (worm_x, worm_y, 20, 20))
    pygame.draw.rect(win, red, (food_x, food_y, 20, 20))
    pygame.display.update()
    clock.tick(fps)
