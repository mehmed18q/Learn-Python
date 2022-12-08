import pygame, sys

pygame.init()

win = pygame.display.set_mode((400,300))
pygame.display.set_caption("First Game")
# color = (R, G, B)
lightblue = (0, 255, 255)
black = (0, 0, 0)

###############= Text =################
win.fill(black)
text = "PyGame"
font = pygame.font.Font(None, 100)
t_s = font.render(text, True, lightblue)
t_r = t_s.get_rect()
t_r.center = (200, 150)
win.blit(t_s, t_r)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


# get fonts
# fonts = pygame.font.get_fonts()
# for f in fonts:
#     print(f)
