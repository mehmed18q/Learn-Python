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
win.fill(white)
pygame.draw.rect(win, red, ((400, 300), (100, 50)), 15)
pygame.draw.circle(win, green, (300, 250), 20, 2)
pygame.draw.ellipse(win, blue, (500, 450, 100, 50), 0)
pygame.draw.polygon(win, (255, 255, 0), ((100, 50), (200, 50), (75, 100), (175, 100)), 0)
pygame.draw.arc(win, green, (600, 100, 50, 50), 1, 3, 1)
pygame.draw.line(win, red, (100, 100), (150, 200), 1)
pygame.draw.aaline(win, red, (50, 100), (150, 150), 1)

# main loop1
# running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
