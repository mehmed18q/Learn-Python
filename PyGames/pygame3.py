import pygame, time, sys

pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("First Game")
# time.sleep(3)
# color = (R, G, B)
red =(255, 0, 0)
green =(0, 255, 0)
blue =(0, 0, 255)
white =(255, 255, 255)
black =(0, 0, 0)
pygame.draw.rect(win, red, ((400, 300), (100, 50)), 15)
pygame.draw.circle(win, green, (300, 250), 20, 0)


# main loop
# running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
