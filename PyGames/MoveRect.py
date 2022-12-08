import pygame, sys

pygame.init()
width = 800
height = 600
white = (255, 255, 255)
cyan = (0, 255, 255)
black = (0, 0, 0)

x_rect = 350
y_rect = 500
speed = 1
fps = 200

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("FirstProject")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # win.fill(white)
    pygame.draw.rect(win, cyan, (x_rect, y_rect, 100, 100))
    if (x_rect >= 0) and (y_rect == 500):
        x_rect += speed
    if (y_rect <= 500) and (x_rect == 700):
        y_rect -= speed
    if (x_rect <= 700) and (y_rect == 0):
        x_rect -= speed
    if (y_rect >= 0) and (x_rect == 0):
        y_rect += speed
    if (y_rect == 500) and (x_rect == 250):
        text = "PyGame"
        font = pygame.font.Font(None, 100)
        t_s = font.render(text, True, cyan)
        t_r = t_s.get_rect()
        t_r.center = (width/2, height/2)
        win.blit(t_s, t_r)
    pygame.display.update()
    clock.tick(fps)

