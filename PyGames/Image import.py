import pygame, time, sys

#initialaiz pygame
from pygame import mouse

pygame.init()

#creat a main root
win = pygame.display.set_mode((800, 600))

#set a title
pygame.display.set_caption("First Game")

# set color of root
white =(255, 255, 255)
win.fill(white)

# set image icon
img = pygame.image.load("a.png")
pygame.display.set_icon(img)

# set background
bg = pygame.image.load("b.jpg")
BG = pygame.transform.scale(bg, (800, 600))
win.blit(BG, (0, 0))

# import a pic on root
img1 = pygame.image.load("cat.png")
img1 = pygame.transform.scale(img1, (128, 128))
win.blit(img1, (500, 400))

# main loop1
# running = True
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONUP:
            #ToDo: move image to 5X
            pass

    pygame.display.update()
