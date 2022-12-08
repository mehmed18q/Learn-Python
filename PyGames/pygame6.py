import pygame, sys

pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("First Game")
# color = (R, G, B)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
win.fill(black)
text = "Game"
font = pygame.font.Font(None, 100)
t_s = font.render(text, True, (0, 255, 255))
t_r = t_s.get_rect()
t_r.center = (400, 300)
win.blit(t_s, t_r)
# win.blit(t_s, (400, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
# fonts = pygame.font.get_fonts()
# for f in fonts:
#     print(f)
