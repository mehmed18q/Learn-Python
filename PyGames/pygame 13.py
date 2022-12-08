import pygame, sys, random
from pygame.locals import *

pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("SimpleGame")
clock = pygame.time.Clock()


red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
p_pos = [370, 500]
e_pos = [random.randint(0, 740), 0]
speed = 10
speed_e = 5
fps = 60

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                p_pos[0] += speed
            if event.key == K_LEFT:
                p_pos[0] -= speed
    if p_pos[0] <= 0:
        p_pos[0] = 0
    if p_pos[0] >= 740:
        p_pos[0] = 740
    # e_pos[1] += speed_e
    # if e_pos[1] == 600:
    #     e_pos[1] = 0
    if (e_pos[1] >= 0) and (e_pos[1] <= 600):
        e_pos[1] += speed_e
    else:
        e_pos[1] = 0
        e_pos[0] = random.randint(0, 740)

    win.fill(black)
    pygame.draw.rect(win, blue,(p_pos[0], p_pos[1], 60, 60))
    pygame.draw.rect(win, red, (e_pos[0], e_pos[1], 60, 60))
    clock.tick(fps)
    pygame.display.update()
