import pygame, time, sys

pygame.init()
# a = (400, 300)
win = pygame.display.set_mode((400, 300))
pygame.display.set_caption("First Game")
# time.sleep(3)

# main loop
running = True
while running :
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
sys.exit()